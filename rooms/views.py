from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Room
from .forms import RoomForm

@login_required
def index(request):
    rooms = Room.objects.all()
    template_name = 'index.html'
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
