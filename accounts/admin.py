from django.contrib import admin
from .models import SubPlan, Subscriber

""" https://stackoverflow.com/questions/48665353/django-1-11-admin-list-filter-to-include-fields-in-another-model """
""" https://djangobook.com/mdj2-django-admin/ """


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'subscription_date', 'subscription_end_date')
    ordering = ('user',)
    search_fields = ('user__username',)


class SubPlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'plan_price')
    ordering = ('plan_name',)


admin.site.register(SubPlan, SubPlanAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
