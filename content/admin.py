from django.contrib import admin
from .models import Categorie, Video


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'featured')
    ordering = ('title',)
    search_fields = ('title',)


admin.site.register(Categorie, CategoryAdmin)
admin.site.register(Video, VideoAdmin)
