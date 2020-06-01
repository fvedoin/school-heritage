from django.contrib import admin
from django.urls import path, include
from users.admin import admin_site_classe

urlpatterns = [
    path('admin/', admin_site_classe.urls),
    path('sistema/', include(('core.urls', 'core'), 'core')),
    path('', include(('users.urls', 'users'), 'users')),
    path('salas/', include(('rooms.urls', 'rooms'), 'rooms')),
    path('itens/', include(('items.urls', 'items'), 'items')),
    path('problemas/', include(('problems.urls', 'problems'), 'problems')),
    path('logs/', include(('logs.urls', 'logs'), 'logs')),
    path('searchableselect/', include('searchableselect.urls')),
]
