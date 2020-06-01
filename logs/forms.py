from django import forms

from .models import Log

class LogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Digite o título do evento'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Digite a descrição do evento'})
        self.fields['problem'].widget = forms.HiddenInput()

    class Meta:
        model = Log
        fields = ['title', 'description', 'problem']
        