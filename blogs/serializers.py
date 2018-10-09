from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                'id',
                'title',
                'gallery',
                'image_url',
                'description',
                'created_at',
        )
        model = Blog