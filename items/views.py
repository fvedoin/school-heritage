from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.decorators import schoolmaster_required
from django.views.generic import View

from .models import Item
from .forms import ItemForm


class ItemIndexView(View):
    template_name = 'items/index.html'

    @method_decorator(login_required)
    def get(self, request):
        items = Item.objects.all()
        form = ItemForm()
        context = {
            'items': items,
            'form': form
        }
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    @method_decorator(schoolmaster_required)
    def post(self, request):
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = ItemForm()
            messages.success(request, 'Item inserido com sucesso!')
        items = Item.objects.all()
        context = {
            'items': items,
            'form': form
        }
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
@method_decorator(schoolmaster_required, name='dispatch')
class ItemEditView(View):
    template_name = 'items/edit.html'

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        elif method == 'delete':
            return self.delete(*args, **kwargs)
        return super(ItemEditView, self).dispatch(*args, **kwargs)

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        context = {}
        form = ItemForm(instance=item)
        context['form'] = form
        return render(request, self.template_name, context)

    def put(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        context = {}
        form = ItemForm(data=request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item alterado com sucesso!')
        context['form'] = form
        return render(request, self.template_name, context)

    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        messages.success(request, 'Item excluído com sucesso!')
        return redirect('items:index')
