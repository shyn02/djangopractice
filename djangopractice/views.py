from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import User

def login_page(request):
    return render(request, "login.html")

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Attempt to find user by email, then authenticate by password
        try:
            user_obj = User.objects.get(email__iexact=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect("/login")

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("/dashboard")
        else:
            messages.error(request, "Invalid email or password.")
            return redirect("/login")
        
@login_required        
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')

@login_required
def change_password(request):
    if request.method == "POST":
        current = request.POST.get("current_password")
        new = request.POST.get("new_password")
        confirm = request.POST.get("confirm_password")

        if not request.user.check_password(current):
            messages.error(request, "Current password is incorrect.")
            return redirect("dashboard")

        if new != confirm:
            messages.error(request, "New passwords do not match.")
            return redirect("dashboard")

        if len(new) < 6:
            messages.error(request, "Password must be at least 6 characters.")
            return redirect("dashboard")

        request.user.set_password(new)
        request.user.save()
        
        update_session_auth_hash(request, request.user)
        messages.success(request, "Password changed successfully.")
        return redirect("dashboard")
    
    return redirect("dashboard")