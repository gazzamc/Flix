from django.db import models
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from utils.slug_gen import unique_slug_generator
from django.contrib.auth.models import User
from django.db import transaction


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
class Video(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=300)
    youtube_link = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    imdb_link = models.CharField(max_length=100)
    tags = TaggableManager()
    image_cover = models.ImageField(upload_to='img')
    image_landscape = models.ImageField(upload_to='img')
    views = models.IntegerField(default=0)
    featured = models.BooleanField()

    # https://stackoverflow.com/questions/1455126/unique-booleanfield-value-in-django
    def save(self, *args, **kwargs):
        if not self.featured:
            return super(Video, self).save(*args, **kwargs)
        with transaction.atomic():
            Video.objects.filter(
                featured=True).update(featured=False)
            return super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Video, on_delete=models.CASCADE)
    slug = models.CharField(max_length=50, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.title


class Likelist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Video, on_delete=models.CASCADE)
    slug = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.item.title


class Dislikelist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Video, on_delete=models.CASCADE)
    slug = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.item.title


def slug_generator(sender, instance, *args, **kwargs):
    """ Generate unique slug """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Video)
