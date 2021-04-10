from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User


def home(request):
    return HttpResponse("Hello User")

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponse('Unauthorized')
    return HttpResponse("Dashboard")

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if(username == ''): return HttpResponse('No Username specified')
        if(password == ''): return HttpResponse('No Password specified')
        user = authenticate(username = username, password = password)
        if(user is None): return HttpResponse('Unauthorized')
        else: 
            return redirect('/username')
            login(request, user)
        return HttpResponse('Your username is: ' + username)
    return render(request, 'authentication/login.html')


def username(request):
    return HttpResponse('Username is: '+ request.user.username)

def logout_user(request):
    logout(request)
    return HttpResponse('You have been logged out!')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if(username == ''): return HttpResponse('No Username specified')
        if(password == ''): return HttpResponse('No Password specified')
        if(email == ''): return HttpResponse('No Email specified')
        User.objects.create_user(username = username, password = password, email = email)
        user = authenticate(username = username, password=password)
        if (User() is None):
            return HttpResponse('Unauthorized')
        else:
            login(request, user)
            return redirect("/dashboard")
    return render(request, 'authentication/register.html')

