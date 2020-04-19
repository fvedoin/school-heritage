from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .forms import CustomUserAuthenticationForm

class Login(auth_views.LoginView):
    authentication_form = CustomUserAuthenticationForm
    form_class = CustomUserAuthenticationForm
