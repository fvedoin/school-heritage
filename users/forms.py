from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import password_validation, get_user_model
from django.contrib.admin.forms import AdminAuthenticationForm
from django import forms


User = get_user_model()


class UserAdminAuthenticationForm(AdminAuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.role == 1:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name}
            )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'phone', 'role', 'is_active']


class UserSessionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite seu nome'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite seu e-mail'})
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control telefone', 'placeholder': 'Digite seu telefone',
             'pattern': '\([0-9]{2}\)[\s][0-9]{4}-[0-9]{4,5}'})
        if self.instance.role != 1:
            self.fields['name'].widget.attrs.update({'readonly': 'true'})

    class Meta:
        model = User
        fields = ['email', 'name', 'phone']


class UserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Digite seu e-mail'}))
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control', 'placeholder': 'Digite sua senha'}),
    )

    error_messages = {
        'invalid_login': 'Informe e-mail e senha válidos.',
        'inactive': 'Usuário inativo.',
    }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Senha antiga',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control',
                   'placeholder': 'Digite sua senha antiga'}),
    )
    new_password1 = forms.CharField(
        label='Nova senha',
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Digite sua nova senha'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label='Confirmação de nova senha',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control',
                                          'placeholder': 'Digite novamente a nova senha'}),
    )
