from django.shortcuts import render, reverse, get_object_or_404
from .models import Faq
from django.contrib.auth.decorators import login_required

# Create your views here.
def contact(request):
    return render(request, 'contact/contact.html')


def faq_page(request):
    faq_list = Faq.objects.all()
    return render(request, 'contact/faq.html', {'faq_list': faq_list})

@login_required
def edit_product(request, faq_list):
    """ Edit FAQ in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Faq, pk=faq_id)
    if request.method == 'POST':
        form = Faq(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)