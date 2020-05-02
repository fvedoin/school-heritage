from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from users.decorators import schoolmaster_required
from .models import Room
from .forms import RoomForm


@login_required
@schoolmaster_required
def index(request):
    rooms = Room.objects.all()
    template_name = 'rooms/index.html'
    form = RoomForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RoomForm()
        messages.success(request, 'Sala inserida com sucesso!')
    context = {
        'rooms': rooms,
        'form': form
    }
    return render(request, template_name, context)


@method_decorator(login_required, name='dispatch')
@method_decorator(schoolmaster_required, name='dispatch')
class RoomEditView(View):
    template_name = 'rooms/edit.html'

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        elif method == 'delete':
            return self.delete(*args, **kwargs)
        return super(RoomEditView, self).dispatch(*args, **kwargs)

    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        context = {}
        form = RoomForm(instance=room)
        context['form'] = form
        return render(request, self.template_name, context)

    def put(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        context = {}
        form = RoomForm(data=request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sala alterada com sucesso!')
        context['form'] = form
        return render(request, self.template_name, context)

    def delete(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        room.delete()
        messages.success(request, 'Sala excluída com sucesso!')
        return redirect('rooms:index')
