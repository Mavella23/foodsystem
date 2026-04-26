from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

ROLE_REDIRECT = {
    'customer': 'customer_dashboard',
    'vendor': 'vendor_dashboard',
    'delivery': 'delivery_dashboard',
    'admin': 'admin_dashboard',
}

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = ROLE_REDIRECT.get(user.role, 'home')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')

@login_required
def customer_dashboard(request):
    return render(request, 'customer_dashboard.html')

@login_required
def vendor_dashboard(request):
    return render(request, 'vendor_dashboard.html')

@login_required
def delivery_dashboard(request):
    return render(request, 'delivery_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
