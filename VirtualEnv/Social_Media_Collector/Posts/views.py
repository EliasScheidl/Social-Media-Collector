from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from Users.models import Profiles
from .models import Images
from django.conf import settings

def feed(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return render(request, "home.html")

def upload(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return render(request, "upload.html")

def viewPost(request):
    UUID = request.session.get('user', None)
    if UUID is None:
        return redirect('../../user/login')
    
    if 'id' in request.GET:
        postId = request.GET['id']
        post = Images.objects.using('htl-schoolpix').filter(id = postId).first() 
        if post is not None:
            user = Profiles.objects.using('htl-schoolpix').filter(id = UUID).first()
            canDelete = user.role == "admin" or post.uploader.id == user.id
            return render(request, "photoview.html", {'post': post, "MEDIA_URL": settings.MEDIA_URL, "canDelete": canDelete})
        
        return HttpResponse("Post does not exist")
        
        
    return HttpResponse("Post not specified")

def manageReportedPost(request):
    UUID = request.session.get('user', None)
    if UUID is None:
        return redirect('../../user/login')
    
    user = Profiles.objects.using('htl-schoolpix').filter(id = str(UUID)).first()

    if user.role is not "admin":
        return HttpResponseForbidden()
    
    return HttpResponse("Report Page")


