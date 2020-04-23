from django.shortcuts import render, get_object_or_404
from content.models import Video, Genre, Watchlist
from content.views import get_watchlist


def search_view(request):
    """ Render search page """
    term = request.GET.get('q')
    genre = request.GET.get('genre')
    watch_list = get_watchlist(request)
    context = {}

    if term is not None:
        results = search_by_term(term)
        result_count = len(results)

        context = {
            'results': results,
            'search_term': term,
            'result_count': result_count,
            'watch_list': watch_list
        }
    elif genre is not None:
        genre_id = Genre.objects.get(name=genre)

        if genre_id is not None:
            results = search_by_genre(genre_id.id)
            result_count = len(results)

            context = {
                'results': results,
                'genre': genre,
                'result_count': result_count,
                'watch_list': watch_list
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
