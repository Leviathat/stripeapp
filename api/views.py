from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from api.models import Item
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(['GET'])
def article(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'index.html', context={'item': item})


@api_view(['GET'])
def buy(request, pk):
    item = Item.objects.get(id=pk)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://www.youtube.com',
        cancel_url='https://www.youtube.com',
    )
    return redirect(session.url)
