from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


@admin.register(AuthorArt)
class AuthorArtAdmin(ModelAdmin):
    pass