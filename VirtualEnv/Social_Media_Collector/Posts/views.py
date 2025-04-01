from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def feed(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return HttpResponse("Hello World")

def post(request):
    if request.session.get('user', None) is None:
        return redirect('../../user/login')
    return HttpResponse("Hello World")