from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from .models import User
import logging


logger = logging.getLogger(__name__)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "student"
            user.set_password(form.cleaned_data["password1"])  
            user.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            logger.info(f"New student registered: {user.email}")
            return redirect("login")
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserRegisterForm()

    return render(request, "auth/register.html", {"form": form})



def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)  
            
            if user:
                login(request, user)
                messages.success(request, f"Welcome, {user.email}!")
                logger.info(f"User logged in: {user.email}")

                return redirect("admin_dashboard" if user.role == "admin" else "student_dashboard")
            else:
                messages.error(request, "Invalid email or password.")
                logger.warning(f"Failed login attempt for email: {email}")
    
    else:
        form = UserLoginForm()

    return render(request, "auth/login.html", {"form": form})

@login_required
def user_logout(request):
    email = request.user.email
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    logger.info(f"User logged out: {email}")
    return redirect("login")
