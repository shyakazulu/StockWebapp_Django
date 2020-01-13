from django import forms
from .models import dbstock


class QuoteForm(forms.ModelForm):
    class Meta:
        model = dbstock
        fields = ["ticker"]