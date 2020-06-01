from django.urls import path
from .views import index, LogEditView

urlpatterns = [
    path('<int:pk>/', index, name='index'),
    path('edit/<int:pk>/', LogEditView.as_view(), name='edit'),
]