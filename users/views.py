from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .forms import CustomUserAuthenticationForm, CustomUserPasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login


class Login(auth_views.LoginView):
    authentication_form = CustomUserAuthenticationForm
    form_class = CustomUserAuthenticationForm


@login_required
def edit_password(request):
    template_name = 'edit_password.html'
    context = {}
    form = CustomUserPasswordChangeForm(data=request.POST or None, user=request.user)
    if form.is_valid():
        form.save()
        user = authenticate(username=request.user.email, password=form.cleaned_data['new_password1'])
        login(request, user)
        messages.success(request, 'Senha alterada com sucesso')
    context['form'] = form
    return render(request, template_name, context)
