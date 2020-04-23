from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Genre, Video, Watchlist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from utils.video import get_video_url
from accounts.models import Subscriber
from itertools import chain


@login_required
def content_view(request):
    """ Display all video content by genre"""
    subscriber = Subscriber.objects.filter(user=request.user.id)
    if subscriber:
        """ Get Featured Content """
        featured_vid = Video.objects.get(featured=True)
        genres = Genre.objects.all()
        all_videos = Video.objects.none()
        watch_list = get_watchlist(request)
        final_video_list = []

        """ Get 20 videos from each category and combine queryset """
        for genre in genres:

            videos = Video.objects.filter(genre=genre)[:20]

            if all_videos is None:
                all_videos = videos
            else:
                """ https://stackoverflow.com/questions/38967599/joining-two-querysets-in-django """
                final_video_list = list(chain(videos, final_video_list))

        content = {
            "videos": final_video_list,
            "genres": genres,
            "watch_list": watch_list,
            "video_url": get_video_url(featured_vid.youtube_link),
            "video_title": featured_vid.title,
            "video_desc": featured_vid.description,
            "video_img": featured_vid.image_landscape,
            "video_link": featured_vid.slug,
        }

        return render(request, 'home.html', content)
    else:
        return redirect(reverse('plans'))

@login_required
def video_view(request, slug):
    """ Display single video content """

    subscriber = Subscriber.objects.filter(user=request.user.id)
    if subscriber:
        video = get_object_or_404(Video, slug=slug)
        content = {
            "title": video.title,
            "slug": video.slug,
            "youtube_link": get_video_url(video.youtube_link),
            "description": video.description,
            "genre": video.genre,
            "video_img": video.image_landscape,
        }

        return render(request, 'video.html', content)
    else:
        return redirect(reverse('plans'))


@login_required
def watchlist_view(request):
    """ Get User Watch List videos """
    videos = get_watchlist(request)

    context = {
        'videos': videos
    }

    return render(request, 'watch-list.html', context)


def get_watchlist(request):

    items = Watchlist.objects.filter(user=request.user)
    videos = Video.objects.none()

    for item in items:
        videos = Video.objects.filter(title=item) | videos

    if len(videos) == 0:
        videos = None

    return videos


@login_required
def add_to_watchlist(request, slug):
    """ Add items to user watch list """
    """ https://stackoverflow.com/questions/56580696/how-to-implement-add-to-wishlist-for-a-product-in-django """

    """ Check if item exist, if so remove """
    try:
        item = Watchlist.objects.get(slug=slug)
        item.delete()
        messages.info(request, 'The item was removed from your watchlist')

    except Watchlist.DoesNotExist:

        video = get_object_or_404(Video, slug=slug)

        Watchlist.objects.get_or_create(
            watch_item=video,
            slug=video.slug,
            user=request.user,
        )

        messages.info(request, 'The item was added to your watchlist')
    return redirect(reverse('watch-list'))
