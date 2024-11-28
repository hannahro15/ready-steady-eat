from django.shortcuts import render, reverse, get_object_or_404
from .models import Faq

# Create your views here.
def contact(request):
    return render(request, 'contact/contact.html')


def faq_page(request):
    faq_list = Faq.objects.all()
    return render(request, 'contact/faq.html', {'faq_list': faq_list})