from rest_framework import generics

from .models import Review
from .serializers import ReviewSerializer

class ListReview(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class DetailReview(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
