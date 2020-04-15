from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Categorie, Video
from django.contrib.auth.decorators import login_required
from utils.video import get_video_url
from accounts.models import Subscriber


@login_required
def content_view(request):
    """ Display all video content """

    """ Get Featured Content """
    featured_vid = Video.objects.get(featured=True)
    categories = Categorie.objects.all()
    all_videos = Video.objects.all()

    content = {
        "videos": all_videos,
        "categories": categories,
        "video_url": get_video_url(featured_vid.youtube_link),
        "video_title": featured_vid.title,
        "video_desc": featured_vid.description,
        "video_img": featured_vid.image_landscape,
        "video_link": featured_vid.slug,
    }

    return render(request, 'home.html', content)

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
        }

        return render(request, 'video.html', content)
    else:
        return redirect(reverse('plans'))
