from django.urls import path
from .views import Login, session_user_edit_password, session_user_edit
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Login.as_view(template_name='sessions/login.html'), name='login'),
    path('alterar-senha/', session_user_edit_password, name='session_user_edit_password'),
    path('alterar-dados/', session_user_edit, name='session_user_edit'),
    path('sair/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),
]
