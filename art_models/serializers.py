from rest_framework import serializers
from .models import *


class ArtGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtGallery
        fields = '__all__'

