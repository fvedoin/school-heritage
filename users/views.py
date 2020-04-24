from django.shortcuts import render, get_object_or_404
import json
from django.http import HttpResponse
from django.contrib.auth import views as auth_views, get_user_model
from .forms import UserAuthenticationForm, UserPasswordChangeForm, UserSessionForm, UserCreateForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login

User = get_user_model()


class Login(auth_views.LoginView):
    authentication_form = UserAuthenticationForm
    form_class = UserAuthenticationForm


@login_required
def session_user_edit_password(request):
    template_name = 'sessions/edit_password.html'
    context = {}
    form = UserPasswordChangeForm(data=request.POST or None, user=request.user)
    if form.is_valid():
        form.save()
        user = authenticate(username=request.user.email, password=form.cleaned_data['new_password1'])
        login(request, user)
        messages.success(request, 'Senha alterada com sucesso')
    context['form'] = form
    return render(request, template_name, context)


@login_required
def session_user_edit(request):
    template_name = 'sessions/edit.html'
    context = {}
    form = UserSessionForm(data=request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Dados salvos com sucesso')
    context['form'] = form
    return render(request, template_name, context)


@login_required
def index(request):
    users = User.objects.exclude(pk=request.user.pk)
    template_name = 'users/index.html'
    context = {'post': False}
    form = UserCreateForm(data=request.POST or None)
    if form.is_valid():
        user = form.save()
        form = UserCreateForm()
        messages.success(request, 'Usuário cadastrado com sucesso.')
        messages.success(request, 'Um e-mail foi enviado para ' + user.email + ' com os dados de acesso.')
    if request.POST:
        context['post'] = True
    context['form'] = form
    context['users'] = users
    return render(request, template_name, context)

@login_required
def edit(request, pk):
    template_name = 'users/edit.html'
    user = get_object_or_404(User, pk=pk)
    context = {}
    form = UserEditForm(data=request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário alterado com sucesso')
    context['form'] = form
    return render(request, template_name, context)

@login_required
def delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    data = {'success': True, 'message': 'Usuário excluído com sucesso'}
    return HttpResponse(json.dumps(data), content_type='application/json')