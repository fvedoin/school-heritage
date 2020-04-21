from django import forms

from .models import Room

class RoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite o nome da sala'})

    class Meta:
        model = Room
        fields = ['name']
