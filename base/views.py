from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm
from . import forms

# Create your views here.

def home(request):
    return HttpResponse("hello world")

def signup(request):
    form = forms.RegistrationForm()
    context = {'form':form, 'page':'signup'}
    
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            HttpResponse("error while saving user")
    
    return render(request, 'base/login_signup.html', context)

def loginUser(request):
    form = forms.LoginForm()
    context = {'form':form}
    return render(request, 'base/login_signup.html', context)
