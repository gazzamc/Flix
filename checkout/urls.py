from django.conf.urls import url
from checkout.views import plans, payment

urlpatterns = [
    url(r'^plans/', plans, name="plans"),
    url(r'^payment/', payment, name="payment")
]