from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import models
from tasks.models import Task, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    tasks = None
    return render(request, 'index.html', {'tasks': tasks})

def login_form(request):
#logs in users/ directed here from register
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = email, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/tasks/')
            else:
                return HttpResponse("Sorry, something is amiss...")

        else:
            return HttpResponse("Ahhhh, nooo, something is quite amiss!")

def register(request):
    #registers in users/ shoots to login

    username = request.POST['fl_name']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['password_confirmation']
    name = []
    name = username.split(' ')
    first_name = name[0]
    last_name = name[1]

    u = User.objects.create_user(username=email, first_name = first_name, last_name = last_name, email = email, password = password)
    u = authenticate(username=email, email = email, password = password)
    login(request, u)
    # django command login
    if u is not None:
        if password != confirm_password:
            return render(request, "index.html", {'errors':"Passwords don't match."})
        else:
            u.save()
            return HttpResponseRedirect('/tasks/')
    else:
        return render(request, "index.html" , {'errors': "Ensure you fill in all the fields"})

    return HttpResponseRedirect('/tasks/')

def logout_form(request):
    logout(request)
    #django logout
    return HttpResponseRedirect('/')
