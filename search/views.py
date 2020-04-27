from django.shortcuts import render
from content.models import Video, Genre


def search_view(request):
    """ Render search page """
    term = request.GET.get('q')
    genre = request.GET.get('genre')
    tag = request.GET.get('tag')
    context = {}

    if term is not None:
        videos = search_by_term(term)
        result_count = len(videos)

        context = {
            "videos": videos,
            "search_term": term,
            "result_count": result_count,
        }
    elif genre is not None:
        genre_id = Genre.objects.get(name=genre)

        if genre_id is not None:
            videos = search_by_genre(genre_id.id)
            result_count = len(videos)

            context = {
                "videos": videos,
                "genre": genre,
                "result_count": result_count,
            }
    elif tag is not None:
        videos = search_by_tag(tag)
        result_count = len(videos)

        context = {
            "videos": videos,
            "tag": tag,
            "result_count": result_count,
        }

    return render(request, "search.html", context)


def search_by_genre(genre):
    """ Get Videos by Genre """
    videos = Video.objects.filter(genre=genre)
    return videos


def search_by_term(term):
    """ Get Videos by term """
    videos = Video.objects.filter(title__icontains=term)
    return videos


def search_by_tag(tag):
    """ Get Videos by tag """
    videos = Video.objects.filter(tags__name__in=[tag])
    return videos
