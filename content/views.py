from django.shortcuts import render, get_object_or_404
from .models import Categorie, Video
from django.contrib.auth.decorators import login_required
from utils.video import get_video_url


@login_required
def content_view(request):
    """ Display all video content """

    categories = Categorie.objects.all()
    content = {
        "categories": categories,
        "test": "This is a test"
    }

    return render(request, 'home.html', content)

@login_required
def video_view(request, slug):
    """ Display single video content """

    video = get_object_or_404(Video, slug=slug)
    content = {
        "title": video.title,
        "slug": video.slug,
        "youtube_link": get_video_url(video.youtube_link),
        "description": video.description,
    }

    return render(request, 'video.html', content)
