from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from Users.models import Profiles, SupabaseUser
from Posts.models import Images
from .models import UserInteractions

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
        inputPasswordHash = request.GET['pw']
        profile = Profiles.objects.using('htl-schoolpix').filter(username = inputUsername).first()

        if profile is not None:
            UUID = str(profile.id)
            user = SupabaseUser.objects.using('htl-schoolpix').filter(id = UUID).first()
            passwordHash = user.encrypted_password
            if inputPasswordHash == passwordHash:
                request.session['user'] = UUID
                return redirect("../../")

    return redirect('../../user/login')

def logoutUser(request):
    logout(request)
    return redirect('../../user/login')

def post(request):
    UUID = request.session.get('user', None)
    if UUID is None:
        return redirect('../../user/login')
    
    user = SupabaseUser.objects.using('htl-schoolpix').filter(id = UUID).first()



    return HttpResponse("Failed")