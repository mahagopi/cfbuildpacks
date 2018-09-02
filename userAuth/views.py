from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    return HttpResponse("|.a.u.t.h.|")

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def logout(request):
    return render(request, 'login.html')