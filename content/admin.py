from django.contrib import admin
from .models import Genre, Video, Likelist, Dislikelist, Watched, Watching


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'views', 'featured')
    ordering = ('title',)
    search_fields = ('title',)

    # https://stackoverflow.com/questions/16014719/adding-a-jquery-script-to-the-django-admin-interface
    class Media:
        js = (
            'libs/js/jquery-3.4.1.min.js',
            'js/admin-imdb.js',
        )


class WatchingAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'time', 'duration',)
    ordering = ('user',)
    search_fields = ('user',)


class WatchedAdmin(admin.ModelAdmin):
    list_display = ('user', 'item',)
    ordering = ('user',)
    search_fields = ('user',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Watching, WatchingAdmin)
admin.site.register(Watched, WatchedAdmin)
