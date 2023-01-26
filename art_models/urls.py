from django.urls import path

from .views import *

urlpatterns = [
    path('', ArtListAPI.as_view()),
]