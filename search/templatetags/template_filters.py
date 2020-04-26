from django import template

register = template.Library()

# https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/
# https://stackoverflow.com/questions/47792373/invalid-filter-error-in-django-custom-template-filter


@register.filter()
def video_in_list(videolist, video):
    count = videolist.filter(title=video).count()
    return count > 0
