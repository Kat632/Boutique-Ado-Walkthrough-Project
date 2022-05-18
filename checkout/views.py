from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag right now")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L0iFID1LBeDoKHEnE0uGHIX25aWhTUXupNSaYGvq2E8O2TSPUIG3YZWbcGRp8r6m2tWVXKhJoVDn3ATbOKk5LGa00rg0O6n7x',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
