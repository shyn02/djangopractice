from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name="login"),
    path('logout/', views.LogoutUserView.as_view(), name="logout"),
    path('', views.DashboardView.as_view(), name="dashboard"),
    path('change-password/', views.ChangePasswordView.as_view(), name="change_password"),
]