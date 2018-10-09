from rest_framework import generics

from .models import Review
from .serializers import ReviewSerializer

class ListReview(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class DetailReview(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
