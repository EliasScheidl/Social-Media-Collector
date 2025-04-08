from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from Users.models import Profiles, SupabaseUser


# Create your views here.
def like(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return HttpResponse("Hello World")

def dislike(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return HttpResponse("Hello World")

def report(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return HttpResponse("Hello World")

def delete(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return HttpResponse("Hello World")

def authenticate(request):
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