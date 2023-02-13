from products.models import Category, Order, OrderItem, Product
from rest_framework import serializers
from users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'discount',
                   'image', 'created_at', 'get_price')

# class ProductCategorySerializer(serializers.ModelSerializer):
#     product = ProductSerializer()
#     category = CategorySerializer()
#     class Meta:
#         model = ProductCategory
#         fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Order
        fields = '__all__'
    
class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    order = OrderSerializer()
    class Meta:
        model = OrderItem
        fields = '__all__'
