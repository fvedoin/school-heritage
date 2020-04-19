from django.urls import path
from .views import index
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index')
]