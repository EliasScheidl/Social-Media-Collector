from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from Users.models import Profiles, SupabaseUser
from Posts.models import Images, Classes, Departments
from .models import UserInteractions
from django.core.files.storage import FileSystemStorage
from ldap3 import Server, Connection, ALL, SIMPLE
from ldap3.core.exceptions import LDAPException
#from django.views.decorators.csrf import csrf_exempt

def like(request):
    UUID = request.session.get('user', None)
    if UUID is None:
        return redirect('../../user/login')
    
    if 'id' in request.GET:
        postId = request.GET['id']
        post = Images.objects.using('htl-schoolpix').filter(id = postId).first() 
        if post is not None:
            interaction = UserInteractions.objects.using('htl-schoolpix').filter(image_id = postId, user_id = UUID).first()
            if interaction is None or interaction.interaction_type != 'like':
                if interaction is not None and interaction.interaction_type == 'dislike':
                    interaction.delete()
                UserInteractions.objects.using('htl-schoolpix').create(image_id = postId, user_id = UUID, interaction_type = 'like')
                return HttpResponse("Success")

    return HttpResponse("Failed")

def dislike(request):
    UUID = request.session.get('user', None)
    if UUID is None:
        return redirect('../../user/login')
    
    if 'id' in request.GET:
        postId = request.GET['id']
        post = Images.objects.using('htl-schoolpix').filter(id = postId).first() 
        if post is not None:
            interaction = UserInteractions.objects.using('htl-schoolpix').filter(image_id = postId, user_id = UUID).first()
            if interaction is None or interaction.interaction_type != 'dislike':
                if interaction is not None and interaction.interaction_type == 'like':
                    interaction.delete()
                UserInteractions.objects.using('htl-schoolpix').create(image_id = postId, user_id = UUID, interaction_type = 'dislike')
                return HttpResponse("Success")

    return HttpResponse("Failed")

def report(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    
    if 'id' in request.GET:
        postId = request.GET['id']
        post = Images.objects.using('htl-schoolpix').filter(id = postId).first() 
        if post is not None:
            post.is_reported = True
            return HttpResponse("Success")

    return HttpResponse("Failed")

def delete(request):
    UUID = request.session.get('user', None)
    if UUID is None:
        return redirect('../../user/login')
    
    if 'id' in request.GET:
        postId = request.GET['id']
        post = Images.objects.using('htl-schoolpix').filter(id = postId).first()
        if post is not None:
            user = Profiles.objects.using('htl-schoolpix').filter(id = str(UUID)).first()
            if user.role == 'admin' or user.id == post.uploader.id:
                post.delete()
                return HttpResponse("Success")

    return HttpResponse("Failed")

def authenticate(request):
    if 'n' in request.GET and 'pw' in request.GET:
        
        inputUsername = request.GET['n']
        inputPassword = request.GET['pw']

        if authenticate_ldap(inputUsername, inputPassword):
            profile = Profiles.objects.using('htl-schoolpix').filter(username = inputUsername).first()

            if profile is None:
                profile = Profiles.objects.using('htl-schoolpix').create(username = inputUsername, role="user")
                print("created new profile for " + inputUsername)

            UUID = str(profile.id)
            request.session['user'] = UUID
            return redirect("../../")
                

    return redirect('../../user/login')

def logoutUser(request):
    logout(request)
    return redirect('../../user/login')

#@csrf_exempt
def post(request):
    UUID = request.session.get('user', None)
    if UUID is None:
        return redirect('../../user/login')
    
    user = Profiles.objects.using('htl-schoolpix').filter(id = UUID).first()

    if request.method == 'POST' and request.FILES.get('image') and 'cap' in request.GET and 'dept' in request.GET and 'class' in request.GET:
        sclass = Classes.objects.using('htl-schoolpix').filter(name=request.GET['class']).first()
        dept = Departments.objects.using('htl-schoolpix').filter(name=request.GET['dept']).first()

        post = Images.objects.using('htl-schoolpix').create(uploader_id = user.id, caption = request.GET['cap'], department_id = dept.id, class_id = sclass.id)
        post.storage_path = 'img_' + post.id
        image = request.FILES['image']
        FileSystemStorage().save(post.storage_path, image)
        return HttpResponse("Success")

    return HttpResponse("Failed") 

def authenticate_ldap(username, password):
    LDAP_SERVER = 'ldaps://ldaps.htlwy.at'
    BASE_DN = 'ou=users,dc=schule,dc=local'

    user_dn = f'uid={username},{BASE_DN}'
    server = Server(LDAP_SERVER, port=636, use_ssl=True, get_info=ALL)

    try:
        conn = Connection(server, user=user_dn, password=password, authentication=SIMPLE, auto_bind=True)
        print("Authenticated successfully.")
        conn.unbind()
        return True
    except LDAPException as e:
        print(f"Authentication failed: {e}")
        return False