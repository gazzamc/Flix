from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from accounts.models import SubPlan, Subscriber
from django.conf import settings
from django.contrib import messages
from .forms import MakePaymentForm
from datetime import datetime
from django.utils.timezone import make_aware
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required
def plans(request):
    """Subscription plans page"""
    plans = SubPlan.objects.all()

    """ Check if user is sub already """

    if request.method == 'POST':
        plan_type = request.POST.get('plan_type')
        plan_price = request.POST.get('plan_price')

        if plan_type is not None:
            request.session['plan_type'] = plan_type
            request.session['plan_price'] = plan_price
            return redirect(reverse('checkout'))

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
        'user_plan': user_plan
    }

    return render(request, 'plans.html', context)

@login_required
def checkout(request):
    """Checkout page"""

    plan_type = request.session.get('plan_type')
    plan_price = request.session.get('plan_price')

    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)

        if payment_form.is_valid():
            try:
                """ Retrieve product """
                """ Removed create product call due to lack of async support in django 1.11, 
                the product wasnt being returned before the following code ran,
                causing an error in create plan. """
                product = stripe.Product.list(limit=1)

                """ Retrieve or create plan """
                plan_list = stripe.Plan.list()
                plan = None

                if len(plan_list) > 0:
                    for plans in plan_list:
                        if plans.nickname == plan_type:
                            plan = plans

                if plan is None:
                    """ retrieve product name """
                    for item in product:
                        for key in item:
                            if key == 'id':
                                product_name = item[key]

                    plan = stripe.Plan.create(
                        nickname=plan_type,
                        product=product_name,
                        amount=int(float(plan_price) * 100),
                        currency='EUR',
                        interval='month',
                        usage_type='licensed',
                    )

                """ Retrieve or Create Customer """
                try:
                    """ If subscriber exists Downgrade/Upgrade """
                    customer = Subscriber.objects.get(user=request.user)
                    subscription_items = stripe.SubscriptionItem.list(
                        subscription=customer.stripe_sub_id,
                    )

                    for item in subscription_items:
                        sub_item_id = item.id

                    """ Get Sub item ID """
                    subscription_item = stripe.SubscriptionItem.retrieve(sub_item_id)

                    """ Modify current subscription with new plan """
                    subscription = stripe.Subscription.modify(
                        subscription_item.subscription,
                        cancel_at_period_end=False,
                        items=[
                            {
                                'id': subscription_item.id,
                                'plan': plan,
                            },
                        ],
                    )

                except Subscriber.DoesNotExist:
                    """ New Subscriber """
                    customer = stripe.Customer.create(
                        email=request.user.email,
                        card=payment_form.cleaned_data['stripe_id'],
                    )

                    """ Update or Create Subscription """
                    subscription = stripe.Subscription.create(
                        customer=customer,
                        items=[
                            {
                                'plan': plan,
                            },
                        ],
                        expand=['latest_invoice.payment_intent'],
                        )

                if subscription.created:
                    """ Get Dates for Subscription """
                    startDate = make_aware(datetime.fromtimestamp(subscription.current_period_start))
                    endDate = make_aware(datetime.fromtimestamp(subscription.current_period_end))

                    """ Check if new subscriber or modifying existing """
                    try:
                        customer = Subscriber.objects.get(user=request.user)

                        """ update user to subscribers table"""
                        Subscriber.objects.filter(pk=customer.pk).update(
                                    plan=SubPlan.objects.get(plan_name=plan_type),
                                    subscription_date=startDate,
                                    subscription_end_date=endDate
                        )

                    except Subscriber.DoesNotExist:
                        messages.error(request, "You have successfully paid")

                        """ Add user to subscribers table"""
                        new_sub = Subscriber.objects.create(
                                    user=request.user,
                                    plan=SubPlan.objects.get(plan_name=plan_type),
                                    stripe_sub_id=subscription.id,
                                    stripe_cus_id=subscription.customer,
                                    subscription_date=startDate,
                                    subscription_end_date=endDate
                        )

                        new_sub.save()

                    """ Clear selected plan from session """
                    request.session['plan_type'] = ''
                    request.session['plan_price'] = ''
                    return redirect(reverse('profile'))
                else:
                    messages.error(request, "Unable to take payment")
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

        else:
            messages.error(request, "We were unable to take a payment with that card!")
    else:

        """ Get selected plan from session """
        plan_type = request.session.get('plan_type')
        plan_price = request.session.get('plan_price')

        payment_form = MakePaymentForm()

    context = {
        'plan': plan_type,
        'total': plan_price,
        'publishable': settings.STRIPE_PUBLISHABLE,
        'payment_form': payment_form,
    }

    return render(request, 'checkout.html', context)


@login_required
def cancel_sub(request):
    """ Cancel Subscription """

    try:
        subscriber = Subscriber.objects.get(user=request.user)

        plan = subscriber.plan

        context = {
            'user_name': request.user.username,
            'plan': plan,
        }

        if request.POST.get('no'):
            return redirect(reverse('profile'))
        elif request.POST.get('yes'):
            """ Get user sub.customer id """
            subscription_id = subscriber.stripe_sub_id
            customer_id = subscriber.stripe_cus_id

            """ Delete from Stripe """
            stripe.Subscription.delete(subscription_id)
            customer = stripe.Customer.delete(customer_id)

            if customer.deleted:
                Subscriber.objects.filter(pk=subscriber.id).delete()
                return redirect(reverse('profile'))

        return render(request, 'cancel.html', context)

    except Subscriber.DoesNotExist:
        return redirect(reverse('profile'))


def get_sub_next_bill_date(request):
    subscriber = Subscriber.objects.get(user=request.user)
    subscription_id = subscriber.stripe_sub_id
    subscription = stripe.Subscription.retrieve(subscription_id)
    date = make_aware(datetime.fromtimestamp(subscription.current_period_end))

    Subscriber.objects.filter(pk=subscriber.pk).update(
                            subscription_end_date=date
                        )

    return date
