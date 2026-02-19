from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
           form=UserCreationForm()
    return render(request,"register.html",{"form":form})
def login_view(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")

    else:
         messages.error(request,"username or password is incorrect")
         return render(request,"login.html")
