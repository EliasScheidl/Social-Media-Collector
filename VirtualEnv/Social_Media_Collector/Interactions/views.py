from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from Users.models import Profiles, SupabaseUser
from Posts.models import Images

def like(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    
    if 'id' in request.GET:
        postId = request.GET['id']
        post = Images.objects.using('htl-schoolpix').filter(id = postId).first() 
        if post is not None:
            #Like logic
            return HttpResponse("Success")

    return HttpResponse("Failed")

def dislike(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    
    if 'id' in request.GET:
        postId = request.GET['id']
        post = Images.objects.using('htl-schoolpix').filter(id = postId).first() 
        if post is not None:
            #Dislike logic
            return HttpResponse("Success")

    return HttpResponse("Failed")

def report(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    
    if 'id' in request.GET:
        postId = request.GET['id']
        post = Images.objects.using('htl-schoolpix').filter(id = postId).first() 
        if post is not None:
            #Report logic
            return HttpResponse("Success")

    return HttpResponse("Failed")

def delete(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    
    if 'id' in request.GET:
        postId = request.GET['id']
        post = Images.objects.using('htl-schoolpix').filter(id = postId).first() 
        if post is not None:
            #Delete logic
            
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