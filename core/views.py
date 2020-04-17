from django.shortcuts import render

def index(request):
    template_name = 'base.html'
    return render(request, template_name)
