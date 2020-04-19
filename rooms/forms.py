from django import forms

from .models import Room

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Digite o nome da sala'

