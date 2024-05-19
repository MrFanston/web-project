from django.forms import ModelForm, Textarea
from .models import Portfolio

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['achievements', 'description']
        widgets = {
            'description': Textarea(attrs={'id': 'default-editor'}),
        }
