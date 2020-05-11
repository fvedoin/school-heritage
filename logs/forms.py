from django import Forms

class LogForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        