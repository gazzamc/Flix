from django import template
from content.models import Watchlist

register = template.Library()

""" https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/ """
""" https://stackoverflow.com/questions/47792373/invalid-filter-error-in-django-custom-template-filter """


@register.filter()
def video_in_watchlist(watchlist, video):
    count = watchlist.filter(title=video).count()
    return count > 0
