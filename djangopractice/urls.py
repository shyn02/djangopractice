from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('login-user/', views.login_user, name="login_user"),
    path('logout-user/', views.logout_user, name="logout_user"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('change-password/', views.change_password, name="change_password"),
]