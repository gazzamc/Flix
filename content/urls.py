from django.conf.urls import url
from .views import content_view, video_view, watchlist_view, add_to_watchlist

urlpatterns = [
    url(r'^$', content_view, name="home"),
    url(r'^watch-list/$', watchlist_view, name="watch-list"),
    url(r'^watch-list/(?P<slug>[-\w\d]+)$', add_to_watchlist),
    url(r'^(?P<slug>[-\w\d]+)', video_view)
]
