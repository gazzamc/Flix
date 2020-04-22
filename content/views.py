from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Genre, Video
from django.contrib.auth.decorators import login_required
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
        final_video_list = []

        """ Get 20 videos from each category and combine queryset """
        for genre in genres:

            videos = Video.objects.filter(genre=genre)[:2]

            if all_videos is None:
                all_videos = videos
            else:
                """ https://stackoverflow.com/questions/38967599/joining-two-querysets-in-django """
                final_video_list = list(chain(videos, final_video_list))

        content = {
            "videos": final_video_list,
            "genres": genres,
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
