from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                'id',
                'name',
                'description',
                'image_url',
                'created_at',
        )
        model = Review