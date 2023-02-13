from rest_framework import serializers
from products.serializers import ProductSerializer
from reviews.models import Reviews

from users.serializers import UserSerializer

class ReviewsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    product = ProductSerializer()
    class Meta:
        model = Reviews
        fields = '__all__'
