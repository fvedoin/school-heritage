from django import forms

from .models import Problem

class ProblemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        CHOICES = [(1, 'Resolvido'), (0, 'Não resolvido')]
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite a descrição do problema'})
        self.fields['item'].widget.attrs.update({'class': 'form-control selectpicker bootstrap-select', 'data-live-search': 'true'})
        self.fields['user'].widget = forms.HiddenInput()
        CHOICES = [(0, 'Não resolvido'),
                   (1, 'Resolvido')]
        self.fields['status'] = forms.ChoiceField(choices=CHOICES)
        self.fields['status'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Problem
        fields = ['description', 'item', 'user', 'status']