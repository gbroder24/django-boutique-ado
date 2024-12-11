from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QUrNEJNgicvIh2wVP9cYWtWT3X9AgicJpU94vcC1uB38euE8dIBpsm3Sekn1HIjWg65lIxhsmCD1uCsMxznifd3007rD8MLyg',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)