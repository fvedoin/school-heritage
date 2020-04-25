from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import views as auth_views, get_user_model
from .forms import UserAuthenticationForm, UserPasswordChangeForm, UserSessionForm, UserCreateForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .decorators import schoolmaster_required

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


@method_decorator(login_required, name='dispatch')
@method_decorator(schoolmaster_required, name='dispatch')
class UserIndexView(View):
    template_name = 'users/index.html'

    def get(self, request):
        users = User.objects.exclude(pk=request.user.pk)
        context = {}
        form = UserCreateForm()
        context['post'] = False
        context['form'] = form
        context['users'] = users
        return render(request, self.template_name, context)

    def post(self, request):
        context = {}
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            form = UserCreateForm()
            messages.success(request, 'Usuário cadastrado com sucesso.')
            messages.success(request, 'Um e-mail foi enviado para ' + user.email + ' com os dados de acesso.')
        users = User.objects.exclude(pk=request.user.pk)
        context['post'] = True
        context['form'] = form
        context['users'] = users
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
@method_decorator(schoolmaster_required, name='dispatch')
class UserEditView(View):
    template_name = 'users/edit.html'

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        elif method == 'delete':
            return self.delete(*args, **kwargs)
        return super(UserEditView, self).dispatch(*args, **kwargs)

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        context = {}
        form = UserEditForm(instance=user)
        context['form'] = form
        return render(request, self.template_name, context)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        context = {}
        form = UserEditForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário alterado com sucesso')
        context['form'] = form
        return render(request, self.template_name, context)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        messages.success(request, 'Usuário excluído com sucesso')
        return redirect('users:index')
