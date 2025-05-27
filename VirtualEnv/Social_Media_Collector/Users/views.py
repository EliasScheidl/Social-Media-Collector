from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import Profiles
from Posts.models import Images
from django.conf import settings
from Posts.views import getPostDates

def login(request):
    return render(request, "login.html")

def account(request):
    UUID = request.session.get('user', None)
    if UUID is None:
        return redirect('../../user/login')
    
    user = Profiles.objects.using('htl-schoolpix').filter(id = UUID).first()
    posts = Images.objects.using('htl-schoolpix').filter(uploader_id = UUID).order_by('created_at')
    
    postDates = getPostDates(posts)

    print(postDates)

    return render(request, "account.html", {'Name': user.username, "Email": user.email, 'dates': postDates, "MEDIA_URL": settings.MEDIA_URL})

