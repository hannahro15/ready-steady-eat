from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from .models import Faq
from .forms import FaqForm, ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def contact(request):
    """ Submit contact form """
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully sent contact form info!')    
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def success(request):
    """ View for successfully sent contact forms! """
    return render(request, 'contact/success.html')


def faq_page(request):
    faq_list = Faq.objects.all()
    return render(request, 'contact/faq.html', {'faq_list': faq_list})


@login_required
def add_faq(request):
    """ Add FAQ """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('faq_page'))

    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added FAQ!')
            return redirect('faq_page')
        else:
            messages.error(request, 'Failed to add faq. Please try again!')
    else:
        form = FaqForm()

    template = 'contact/add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_faq(request, faq_id):
    """ Edit an faq """
    faq = get_object_or_404(Faq, pk=faq_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated FAQ!')
            return redirect('faq_page')
        else:
            messages.error(request, 'Failed to update FAQ.')
    else:
        form = FaqForm(instance=faq)

    template = 'contact/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """ Delete an faq """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('faq_page')

    faq = get_object_or_404(Faq, pk=faq_id)
    faq.delete()
    messages.success(request, 'FAQ deleted!')
    return redirect('faq_page')
