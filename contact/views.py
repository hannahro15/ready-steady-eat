from django.shortcuts import render, reverse, get_object_or_404
from .models import Faq
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def contact(request):
    return render(request, 'contact/contact.html')


def faq_page(request):
    faq_list = Faq.objects.all()
    return render(request, 'contact/faq.html', {'faq_list': faq_list})


def edit_faq(request, faq_id):
    """ Edit an faq """
    faq = get_object_or_404(Faq, pk=faq_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('faq_page', args=[faq.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = FaqForm(instance=faq)
        messages.info(request, f'You are editing {faq.id}')

    template = 'products/edit_product.html'
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
        return redirect(reverse('delete_faq'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'FAQ deleted!')
    return redirect(reverse('faq_page'))
