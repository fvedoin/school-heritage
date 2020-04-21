from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    template_name = 'layouts/base.html'
    return render(request, template_name)
