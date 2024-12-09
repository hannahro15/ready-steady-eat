from django import forms
from .widgets import CustomClearableFileInput
from .models import Faq, Contact


class FaqForm(forms.ModelForm):

    class Meta:
        model = Faq
        fields = '__all__'