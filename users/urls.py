from django.urls import path
from .views import Login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Login.as_view(template_name='login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),
]
