from django.db import models
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from utils.slug_gen import unique_slug_generator


class Categorie(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
class Video(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=300)
    youtube_link = models.CharField(max_length=100)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    imdb_link = models.CharField(max_length=100)
    tags = TaggableManager()
    image = models.ImageField(upload_to='media/img')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Video)
