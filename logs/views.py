from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.decorators import schoolmaster_required
from django.views.generic import View

from items.models import Item
from problems.models import Problem
from logs.models import Log

from logs.forms import LogForm


@login_required
@schoolmaster_required
def index(request, pk):
    template_name = 'logs/index.html'
    logs = Log.objects.filter(problem_id=pk)
    context = {}
    form = LogForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LogForm()
        messages.success(request, 'Evento inserido com sucesso!')
    problem = Problem.objects.get(pk=pk)
    context['problem'] = problem
    context['item'] = Item.objects.get(pk=problem.item_id)
    context['logs'] = logs
    context['form'] = form
    context['form'].fields['problem'].initial = pk

    return render(request, template_name, context)

@method_decorator(login_required, name='dispatch')
@method_decorator(schoolmaster_required, name='dispatch')
class LogEditView(View):
    template_name = 'logs/edit.html'

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        elif method == 'delete':
            return self.delete(*args, **kwargs)
        return super(LogEditView, self).dispatch(*args, **kwargs)

    def get(self, request, pk):
        log = get_object_or_404(Log, pk=pk)
        context = {}
        form = LogForm(instance=log)
        context['form'] = form
        context['problem_id'] = log.problem_id
        return render(request, self.template_name, context)

    def put(self, request, pk):
        log = get_object_or_404(Log, pk=pk)
        context = {}
        context['problem_id'] = log.problem_id
        form = LogForm(data=request.POST, instance=log)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento alterado com sucesso!')
        context['form'] = form
        return render(request, self.template_name, context)
