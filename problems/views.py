from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Problem
from .forms import ProblemForm

@login_required
def index(request):
    problems = Problem.objects.all()
    template_name = 'problems/index.html'
    form = ProblemForm(request.POST or None)
    if form.is_valid():
        #form['usuario_id'] = request.POST['usuario']
        form.save()
        form = ProblemForm()
        messages.success(request, 'Problema inserido com sucesso!')
    context = {
        'problems': problems,
        'form': form,
        'user': request.user.id
    }
    return render(request, template_name, context)

