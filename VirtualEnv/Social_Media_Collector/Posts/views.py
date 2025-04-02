from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect

# Create your views here.
def feed(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return HttpResponse("Hello World")

def upload(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return HttpResponse("Hello World")

def viewPost(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return HttpResponse("Hello World")

def manageReportedPost(request):
    if request.session.get('isAdmin', "False") is "False":
        return HttpResponseForbidden()
    return HttpResponse("Hello World")