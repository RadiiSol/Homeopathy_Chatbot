from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def go_home(request):
    if request.user.is_authenticated:
        return HttpResponse("<h3> Welcome User, You are logged in....</h3> <a href='accounts/signout'> Click here to LOGOUT</a> <br><br> <a href='accounts/login'>Click here to LOGIN..</a> <br> <a href='accounts/signup'>Click here to SIGNUP..</a>")
    return HttpResponse(" <a href='accounts/login'>Click here to LOGIN..</a> <br> <a href='accounts/signup'>Click here to SIGNUP..</a>")

def login(request):
    if request.method == "POST":
        info = request.POST['info']
        password = request.POST['password']

        if '@' in info:
            email = info
            if User.objects.filter(email=email).exists():
                username = User.objects.filter(email=email)[0].username
            else:
                username = "not found"
        else:
            username = info

        print("")
        print("")
        print("Username: " + username)
        print("Password: " + password)
        print("")
        print("")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('go_home')
        else:
            return render(request, 'index.html', {'error': 'Record not Valid'})


    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def signout(request):
    logout(request)
    return redirect('go_home')

