from rest_framework import generics

from .models import Gallery
from .serializers import GallerySerializer

class ListGallery(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer