from django.urls import path
from .views import Login, edit_password
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Login.as_view(template_name='login.html'), name='login'),
    path('alterar-senha/', edit_password, name='edit_password'),
    path('sair/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),
]
