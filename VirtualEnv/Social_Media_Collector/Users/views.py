from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import Profiles
from Posts.models import Images
import math

def login(request):
    return render(request, "login.html")

def account(request):
    UUID = request.session.get('user', None)
    if UUID is None:
        return redirect('../../user/login')
    
    user = Profiles.objects.using('htl-schoolpix').filter(id = UUID).first()
    posts = Images.objects.using('htl-schoolpix').filter(uploader_id = UUID)
    print(posts.count())
    
    rows = [[None for _ in range(3)] for _ in range(math.ceil(posts.count() / 3))]

    for i in range(math.ceil(posts.count() / 3)):
        for j in range(posts.count() % ((i+1) * 3)):
            rows[i][j] = posts[i * 3 + j]

    print(rows)
    return render(request, "account.html", {'Name': user.username, "Email": user.email, 'rows': rows})