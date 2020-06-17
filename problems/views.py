from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.decorators import schoolmaster_required
from django.views.generic import View

from .models import Problem
from logs.models import Log
from users.models import CustomUser
from .forms import ProblemForm
from logs.forms import LogForm

@login_required
def index(request):
    if request.user.role != 1:
        problems = Problem.objects.filter(user_id=request.user.id)
    else:
        problems = Problem.objects.all()
    template_name = 'problems/index.html'
    context = {}
    form = ProblemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProblemForm()
        problem_id = Problem.objects.latest('id')
        log = Log(title='Problema criado', description='', problem=problem_id)
        log.save()
        messages.success(request, 'Problema inserido com sucesso!')
    context['problems'] = problems
    context['form'] = form
    context['form'].fields['user'].initial = request.user.id
    
    return render(request, template_name, context)

@method_decorator(login_required, name='dispatch')
@method_decorator(schoolmaster_required, name='dispatch')
class ProblemEditView(View):
    template_name = 'problems/edit.html'

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        elif method == 'delete':
            return self.delete(*args, **kwargs)
        return super(ProblemEditView, self).dispatch(*args, **kwargs)

    def get(self, request, pk):
        problem = get_object_or_404(Problem, pk=pk)
        context = {}
        form = ProblemForm(instance=problem)
        context['form'] = form
        return render(request, self.template_name, context)

    def put(self, request, pk):
        problem = get_object_or_404(Problem, pk=pk)
        context = {}
        form = ProblemForm(data=request.POST, instance=problem)
        if form.is_valid():
            form.save()
            messages.success(request, 'Problema alterado com sucesso!')
        context['form'] = form
        return render(request, self.template_name, context)

    def delete(self, request, pk):
        problem = get_object_or_404(Problem, pk=pk)
        problem.delete()
        messages.success(request, 'Problema excluído com sucesso!')
        return redirect('problems:index')