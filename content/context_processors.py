from .models import Genre

""" https://stackoverflow.com/questions/34902707/how-can-i-pass-data-to-django-layouts-like-base-html-without-having-to-provi/34903331 """
def add_genres_to_context(request):
    genres = Genre.objects.all().order_by('name')
    context = {
        'genres': genres,
    }
    return context
