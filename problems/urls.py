from django.urls import path
from .views import index, ProblemEditView

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', ProblemEditView.as_view(), name='edit'),
]