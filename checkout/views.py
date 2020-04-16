from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import SubPlan, Subscriber

@login_required
def plans(request):
    """Subscription plans page"""
    plans = SubPlan.objects.all()

    """ Check if user is sub already """

    try:
        subscriber = Subscriber.objects.get(user=request.user.id)
    except Subscriber.DoesNotExist:
        subscriber = None

    if subscriber:
        user_plan = subscriber.plan
    else:
        user_plan = None

    context = {
        'plans': plans,
        'curr_plan': user_plan
    }

    return render(request, 'plans.html', context)

@login_required
def payment(request):
    """Subscription plans page"""
    plan_type = request.POST.get('plan_type')

    return render(request, 'checkout.html', {'plan': plan_type})
