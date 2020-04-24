from django.contrib import admin
from .models import Genre, Video, Likelist, Dislikelist


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'views', 'featured')
    ordering = ('title',)
    search_fields = ('title',)

    class Media:
        js = (
            'libs/js/jquery-3.4.1.min.js',
            'js/admin-imdb.js',
        )


admin.site.register(Genre, GenreAdmin)
admin.site.register(Video, VideoAdmin)
