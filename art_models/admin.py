from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


@admin.register(AuthorArt)
class AuthorArtAdmin(ModelAdmin):
    pass


@admin.register(Tag)
class AuthorArtAdmin(ModelAdmin):
    pass


@admin.register(Category)
class AuthorArtAdmin(ModelAdmin):
    pass


class PostImageAdmin(admin.StackedInline):
    model = ArtAlbum


@admin.register(ArtGallery)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = ArtGallery


@admin.register(ArtAlbum)
class PostImageAdmin(admin.ModelAdmin):
    pass