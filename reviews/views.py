from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from users.permissions import ReadOnly
from reviews.models import Reviews
from reviews.serializers import ReviewsSerializer
# Create your views here.

class ReviewsView(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsAdminUser | ReadOnly]