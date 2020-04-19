from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.sites import AdminSite

from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserAdminAuthenticationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_schoolmaster', 'is_active',)
    list_filter = ('email', 'is_schoolmaster', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name')}),
        ('Permissions', {'fields': ('is_schoolmaster', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_schoolmaster', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class CustomUserAdminSite(AdminSite):
    login_form = CustomUserAdminAuthenticationForm
    def has_permission(self, request):
        """
        Return True if the given HttpRequest has permission to view
        *at least one* page in the admin site.
        """
        return request.user.is_active and request.user.is_schoolmaster


admin_site_classe = CustomUserAdminSite()
admin_site_classe.register(CustomUser, CustomUserAdmin)
