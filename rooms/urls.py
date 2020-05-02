from django.urls import path
from .views import index, RoomEditView

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', RoomEditView.as_view(), name='edit'),
]