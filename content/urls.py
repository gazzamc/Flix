from django.conf.urls import url
from .views import content_view, video_view, watchlist_view, add_to_watchlist, like_dislike_video

urlpatterns = [
    url(r'^$', content_view, name="home"),
    url(r'^watch-list/$', watchlist_view, name="watch-list"),
    url(r'^watch-list/(?P<slug>[-\w\d]+)$', add_to_watchlist),
    url(r'^like/(?P<slug>[-\w\d]+)$', like_dislike_video, name='like'),
    url(r'^dislike/(?P<slug>[-\w\d]+)$', like_dislike_video, name='dislike'),
    url(r'^(?P<slug>[-\w\d]+)', video_view)
]
