from django import forms

from .models import Item

class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite o nome do item'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite a descrição do item'})
        self.fields['room'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Item
        fields = ['name', 'description', 'room']