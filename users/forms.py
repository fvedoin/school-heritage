from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import password_validation, get_user_model
from django.contrib.admin.forms import AdminAuthenticationForm
from django import forms
from core.utils import generate_password
from core.mail import send_mail_template

User = get_user_model()


class UserAdminAuthenticationForm(AdminAuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.role == 1:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name}
            )


class UserCreateForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        password = generate_password()
        user.set_password(password)
        if commit:
            user.save()
            template_name = 'users/create_user_mail.html'
            subject = 'Login no sistema de controle de patrimônio'
            context = {
                'user': user,
                'password': password
            }
            send_mail_template(subject, template_name, context, [user.email])
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite seu nome'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite seu e-mail'})
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control telefone', 'placeholder': 'Digite seu telefone',
             'pattern': '\([0-9]{2}\)[\s][0-9]{4}-[0-9]{4,5}'})
        self.fields['role'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = User
        fields = ['email', 'name', 'phone', 'role', 'is_active']


class UserEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite seu nome'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite seu e-mail'})
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control telefone', 'placeholder': 'Digite seu telefone',
             'pattern': '\([0-9]{2}\)[\s][0-9]{4}-[0-9]{4,5}'})
        self.fields['role'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})

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
