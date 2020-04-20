from django.conf.urls import url
from .views import plans, checkout, cancel_sub

urlpatterns = [
    url(r'^plans/', plans, name="plans"),
    url(r'^payment/', checkout, name="checkout"),
    url(r'^cancel-sub/', cancel_sub, name="cancel-sub"),
]
