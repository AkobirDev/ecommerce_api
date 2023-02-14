from products.models import Category, Order, OrderItem, Product
from rest_framework import serializers
from users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.StringRelatedField(many=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'discount',
                  'rating','image','get_price', 'created_at', )

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Order
        fields = ('id', 'user', 'is_ordered', 'ordered_at',)
    
class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    order = OrderSerializer()
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'order', 'quantity', 'get_total_product_price')
