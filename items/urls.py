from django.urls import path
from .views import index, ItemEditView

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', ItemEditView.as_view(), name='edit'),
]