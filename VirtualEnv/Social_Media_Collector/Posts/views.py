from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from Users.models import Profiles
from .models import Images

def feed(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return render(request, "home.html")

def upload(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return render(request, "upload.html")

def viewPost(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    
    if 'id' in request.GET:
        postId = request.GET['id']
        post = Images.objects.using('htl-schoolpix').filter(id = postId).first() 
        if post is not None:
            #Viewing logic
            return HttpResponse("Viewing post " + postId)
        
    return HttpResponse("Post does not exist")

def manageReportedPost(request):
    UUID = request.session.get('user', None)
    if UUID is None:
        return redirect('../../user/login')
    
    user = Profiles.objects.using('htl-schoolpix').filter(id = str(UUID)).first()

    if user.role is not "admin":
        return HttpResponseForbidden()
    
    return HttpResponse("Report Page")


