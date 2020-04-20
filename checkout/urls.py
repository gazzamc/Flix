from django.conf.urls import url
from .views import plans, checkout

urlpatterns = [
    url(r'^plans/', plans, name="plans"),
    url(r'^payment/', checkout, name="checkout")
]
