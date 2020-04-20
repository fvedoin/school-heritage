from django.urls import path
from .views import Login, user_logged_edit_password, user_logged_edit
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Login.as_view(template_name='login.html'), name='login'),
    path('alterar-senha/', user_logged_edit_password, name='user_logged_edit_password'),
    path('alterar-dados/', user_logged_edit, name='user_logged_edit'),
    path('sair/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),
]
