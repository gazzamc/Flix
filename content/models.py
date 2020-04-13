from django.db import models
from taggit.managers import TaggableManager


class Categorie(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    youtube_link = models.CharField(max_length=100)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    imdb_link = models.CharField(max_length=100)
    tags = TaggableManager()
    image = models.ImageField(upload_to='media/img')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
