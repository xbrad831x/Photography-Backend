from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                'id',
                'title',
                'image_url',
                'description',
                'created_at',
        )
        model = Blog