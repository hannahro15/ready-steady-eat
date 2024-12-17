from django import forms
from .models import Faq, Contact
from django.forms import ModelForm, TextInput, EmailInput


class FaqForm(forms.ModelForm):

    class Meta:
        model = Faq
        fields = ['question', 'answer']

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['firstName', 'lastName', 'email', 'phone', 'comments']
        widgets = {
            'firstName': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1000px; margin-bottom: 10px;',
                'placeholder': 'First Name'
                }),

            'lastName': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1000px; margin-bottom: 10px;',
                'placeholder': 'Last Name'
                }),
            
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 1000px; margin-bottom: 10px;',
                'placeholder': 'Email'
                }),

            'phone': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1000px; margin-bottom: 10px;',
                'placeholder': 'Phone'
                }),

            'comments': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 1000px;',
                'placeholder': 'Please enter any comments here'
                }),
        }