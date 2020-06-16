from django.urls import path
from .views import ItemIndexView, ItemEditView

urlpatterns = [
    path('', ItemIndexView.as_view(), name='index'),
    path('<int:pk>/', ItemEditView.as_view(), name='edit'),
]