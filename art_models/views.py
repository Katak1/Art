from rest_framework.generics import ListAPIView

from .models import *
from .serializers import *

class ArtListAPI(ListAPIView):
    queryset = ArtGallery.objects.all()
    serializer_class = ArtGallerySerializer
