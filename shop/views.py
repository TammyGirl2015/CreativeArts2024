import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

stripe.api_key = settings.STRIPE_SECRET_KEY

# Checkout View
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

# Index HTML View
def index(request):
    return render(request, 'shop/index.html')  

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})