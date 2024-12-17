from django import forms
from .models import Faq, Contact
from django.forms import ModelForm


class FaqForm(forms.ModelForm):

    class Meta:
        model = Faq
        fields = ['question', 'answer']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstName', 'lastName', 'email', 'phone', 'comments']