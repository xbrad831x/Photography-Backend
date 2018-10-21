from rest_framework import generics

from .models import Homepic
from .serializers import HomepicSerializer

class ListHomepic(generics.ListAPIView):
    queryset = Homepic.objects.all()
    serializer_class = HomepicSerializer
