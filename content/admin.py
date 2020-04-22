from django.contrib import admin
from .models import Genre, Video


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'views', 'featured')
    ordering = ('title',)
    search_fields = ('title',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Video, VideoAdmin)
