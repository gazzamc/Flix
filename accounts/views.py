from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Subscriber
from accounts.forms import UserLoginForm, UserRegistrationForm
from content.views import content_view
from checkout.views import get_sub_next_bill_date
from datetime import date


def index(request):
    """ Return the index.html if subscription valid otherwise redirect to plans page"""

    # Check if user is logged in
    if request.user.is_authenticated:
        # Check if subscription exists using user id
        # https://stackoverflow.com/questions/12615154/how-to-get-the-currently-logged-in-users-user-id-in-django
        subscriber = Subscriber.objects.filter(user=request.user.id)
        if subscriber:
            return content_view(request)
        else:
            return redirect(reverse('plans'))
    else:
        return render(request, 'index.html')

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})

@login_required
def user_profile(request):
    """The user's profile page"""

    try:
        subscriber = Subscriber.objects.get(user=request.user.id)
    except Subscriber.DoesNotExist:
        subscriber = None

    if subscriber:
        user_plan = subscriber.plan

        """ Check if next bill date valid, if not get new date """
        todays_date = date.today()
        next_bill_date = subscriber.subscription_end_date

        if next_bill_date < todays_date:
            """ Get new date and update current subscription """
            next_bill_date = get_sub_next_bill_date(request)

    else:
        user_plan = None
        next_bill_date = None

    user = User.objects.get(email=request.user.email)

    context = {
        "profile": user,
        "user_plan": user_plan,
        "next_billing": next_bill_date
    }
    return render(request, 'profile.html', context)
