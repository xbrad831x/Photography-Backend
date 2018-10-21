from rest_framework import serializers
from .models import Homepic

class HomepicSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                'title',
                'image_url',
        )
        model = Homepic