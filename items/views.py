from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import ItemForm

@login_required
def index(request):
    items = Item.objects.all()
    template_name = 'items/index.html'
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ItemForm()
        messages.success(request, 'Item inserido com sucesso!')
    context = {
        'items': items,
        'form': form
    }
    return render(request, template_name, context)
