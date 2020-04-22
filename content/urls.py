from django.conf.urls import url
from .views import content_view, video_view

urlpatterns = [
    url(r'^$', content_view, name="home"),
    url(r'^(?P<slug>[-\w\d]+)', video_view)
]
