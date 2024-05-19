# forms.py
from django import forms
from .models import Portfolio
from tinymce.widgets import TinyMCE

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['description']
        widgets = {'description': TinyMCE(attrs={'cols': 80, 'rows': 30})}

