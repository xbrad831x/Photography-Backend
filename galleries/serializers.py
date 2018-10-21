from rest_framework import serializers
from .models import Gallery

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                'title',
                'gallery',
                'image_url',
        )
        model = Gallery