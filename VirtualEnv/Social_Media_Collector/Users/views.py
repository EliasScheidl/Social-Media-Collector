from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login

def login(request):
   if request.session.get('user', None) is not None:
        return redirect('../../')
   return HttpResponse("Hello World")

def account(request):
    if request.session.get('user', None) is None:
        return redirect('../login')
    return HttpResponse("Hello World")