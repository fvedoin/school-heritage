from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.decorators import schoolmaster_required


@login_required
@schoolmaster_required
def index(request):
    template_name = 'reports/index.html'
    context = {}
    return render(request, template_name, context)
