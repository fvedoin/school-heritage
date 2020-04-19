from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import password_validation
from django.contrib.admin.forms import AdminAuthenticationForm
from django import forms
from .models import CustomUser


class CustomUserAdminAuthenticationForm(AdminAuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_schoolmaster:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name}
            )


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'name',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name',)


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Digite seu e-mail'}))
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control', 'placeholder': 'Digite sua senha'}),
    )

    error_messages = {
        'invalid_login': 'Informe e-mail e senha válidos',
        'inactive': 'Usuário inativo',
    }


class CustomUserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Senha antiga',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control', 'placeholder': 'Digite sua senha antiga'}),
    )
    new_password1 = forms.CharField(
        label='Nova senha',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Digite sua nova senha'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label='Confirmação de nova senha',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Digite novamente a nova senha'}),
    )
