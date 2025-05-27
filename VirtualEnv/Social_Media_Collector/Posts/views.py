from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from Users.models import Profiles
from .models import Images
from django.conf import settings
import math

def feed(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    
    posts = Images.objects.using('htl-schoolpix').order_by('created_at')
    
    postDates = getPostDates(posts)

    return render(request, "home.html", {'dates': postDates, "MEDIA_URL": settings.MEDIA_URL})

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
    
    posts = Images.objects.using('htl-schoolpix').filter(is_reported = True).order_by('created_at')
    
    postDates = getPostDates(posts)

    return render(request, "home.html", {'dates': postDates, "MEDIA_URL": settings.MEDIA_URL})

def getPostDates(posts):
    dates = list(set([post.created_at.date for post in posts]))
    postDates = [None for _ in range(len(dates))]

    for dateIndex in range(len(dates)):
        postsAtDate = [post for post in posts if post.created_at.date == dates[dateIndex]]
        rows = [[None for _ in range(3)] for _ in range(math.ceil(len(postsAtDate) / 3))]
        postsleft = len(postsAtDate)
        for i in range(math.ceil(len(postsAtDate) / 3)):
            n=3
            if postsleft <3:
                n = postsleft
            postsleft -= 3

            for j in range(n):
                rows[i][j] = postsAtDate[i * 3 + j]
        postDates[dateIndex] = rows
    return postDates

