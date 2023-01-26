from django.db import models
from django.template.defaultfilters import slugify

from account.models import User


class AuthorArt(models.Model):
    full_name = models.CharField(max_length=150)

    def __str__(self):
        return self.full_name


class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, primary_key=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, primary_key=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ArtGallery(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='users')
    category = models.ManyToManyField(Category,
                                      related_name='categories')
    tag = models.ManyToManyField(Tag, related_name='tags')
    author_art = models.ManyToManyField(AuthorArt, related_name='authors')
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField()
    size_x = models.PositiveIntegerField()
    size_y = models.PositiveIntegerField()
    publication_date = models.DateTimeField(auto_now=True)
    image = models.FileField(blank=True)


class ArtAlbum(models.Model):
    art = models.ForeignKey(ArtGallery, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')