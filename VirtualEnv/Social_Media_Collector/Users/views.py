from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login

# Create your views here.
def login(request):
   return HttpResponse("Hello World")

def account(request):
    if request.session.get('user', None) is None:
        return redirect('../login')
    return HttpResponse("Hello World")