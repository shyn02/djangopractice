from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model  
        
class LoginUserView(View):
    def get(self, request):
        return render(request, "login.html")
    
    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj_email = get_user_model.objects.get(email__iexact=email)
            if user_obj_email:
                user = authenticate(request, username=user_obj_email.username, password=password)
            else:
                user = authenticate(request, username=email, password=password)
        except get_user_model.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect("/login")

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("/dashboard")
        else:
            messages.error(request, "Invalid email or password.")
            return redirect("/login")

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

class LogoutUserView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully.")
        return redirect('login')
    
class ChangePasswordView(LoginRequiredMixin, View):
    def get(self, request):
        return redirect("dashboard")
    
    def post(self, request):
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