from django import forms
from .models import Faq, Contact


class FaqForm(forms.ModelForm):

    class Meta:
        model = Faq
        fields = ['question', 'answer']

