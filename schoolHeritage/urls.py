from django.contrib import admin
from django.urls import path, include
from users.admin import admin_site_classe

urlpatterns = [
    path('admin/', admin_site_classe.urls),
    path('', include(('users.urls', 'users'), 'users')),
    path('salas/', include(('rooms.urls', 'rooms'), 'rooms')),
    path('itens/', include(('items.urls', 'items'), 'items')),
    path('problemas/', include(('problems.urls', 'problems'), 'problems')),
    path('relatorio/', include(('reports.urls', 'reports'), 'reports')),
    path('logs/', include(('logs.urls', 'logs'), 'logs')),
]
