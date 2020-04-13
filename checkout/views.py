from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def plans(request):
    """Subscription plans page"""
    return render(request, 'plans.html')

@login_required
def payment(request):
    """Subscription plans page"""
    return render(request, 'checkout.html')
