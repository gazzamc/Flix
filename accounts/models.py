from django.db import models
from django.contrib.auth.models import User


class SubPlan(models.Model):
    plan_name = models.CharField(max_length=50)
    plan_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.plan_name


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubPlan, on_delete=models.CASCADE)
    stripe_sub_id = models.CharField(max_length=50)
    stripe_cus_id = models.CharField(max_length=50)
    subscription_date = models.DateField()
    subscription_end_date = models.DateField()

    def __str__(self):
        return self.user.email
