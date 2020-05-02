from django.urls import path
from .views import index, ProblemEditView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', ProblemEditView.as_view(), name='edit'),
]