from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def dashboard (request):
    return render (request, 'dashboard.html')
def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully")
            return redirect('login')
    else:
           form= CustomUserCreationForm()
    return render(request,"register.html",{"form": form})
def login_view(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')   # 👈 HAPA NDIO IMPORTANT

        else:
            messages.error(request, "Username or password is incorrect")

    return render(request, "login.html")
            
           
    