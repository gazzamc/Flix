from django.shortcuts import render, get_object_or_404
from content.models import Video, Genre, Watchlist
from content.views import get_watchlist, get_likelist, get_dislikelist


def search_view(request):
    """ Render search page """
    term = request.GET.get('q')
    genre = request.GET.get('genre')
    tag = request.GET.get('tag')
    watch_list = get_watchlist(request)
    like_list = get_likelist(request)
    dislike_list = get_dislikelist(request)
    context = {}

    if term is not None:
        videos = search_by_term(term)
        result_count = len(videos)

        context = {
            "videos": videos,
            "search_term": term,
            "result_count": result_count,
            "watch_list": watch_list,
            "like_list": like_list,
            "dislike_list": dislike_list,
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
                "watch_list": watch_list,
                "like_list": like_list,
                "dislike_list": dislike_list,
            }

    return render(request, "search.html", context)


def search_by_genre(genre):
    """ Get Videos by Genre """
    videos = Video.objects.filter(genre=genre)
    return videos


def search_by_term(term):
    """ Get Videos by term """
    videos = Video.objects.filter(title__contains=term)
    return videos
