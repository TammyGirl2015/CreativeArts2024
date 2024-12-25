import stripe
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    if request.method == "POST":
        try:
            # Create a Stripe Payment Intent
            intent = stripe.PaymentIntent.create(
                amount=1000,  # Amount in cents
                currency='usd',
                metadata={'user_id': request.user.id} if request.user.is_authenticated else None
            )
            return JsonResponse({'clientSecret': intent['client_secret']})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return render(request, 'shop/checkout.html')

def index(request):
    return render(request, 'shop/index.html')  