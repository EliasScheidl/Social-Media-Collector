from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


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
    return HttpResponse("Hello World")