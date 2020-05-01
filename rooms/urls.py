from django.urls import path
from .views import index, RoomEditView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', RoomEditView.as_view(), name='edit'),
]