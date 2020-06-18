from django.urls import path
from .views import index, searchProblemsCreated, searchProblemsResolved

urlpatterns = [
    path('', index, name='index'),
    path('buscar-problemas-criados', searchProblemsCreated, name='searchProblemsCreated'),
    path('buscar-problemas-resolvidos', searchProblemsResolved, name='searchProblemsResolved')
]