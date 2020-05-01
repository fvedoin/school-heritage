from django import forms

from .models import Problem

class ProblemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite a descrição do problema'})
        self.fields['item'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Problem
        fields = ['description', 'item']