from django.shortcuts import render
from products.permissions import ReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from products.serializers import CategorySerializer, OrderItemSerializer, OrderSerializer , ProductSerializer
from products.models import Category, Order, OrderItem, Product 
# Create your views here

class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser | ReadOnly]

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser | ReadOnly]

# class ProductCategoryList(ListCreateAPIView):
#     queryset = ProductCategory.objects.all()
#     serializer_class = ProductCategorySerializer

# class ProductCategoryDetail(RetrieveUpdateDestroyAPIView):
#     queryset = ProductCategory.objects.all()
#     serializer_class = ProductCategorySerializer

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser | ReadOnly]


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated | ReadOnly]

class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderDetailView(ListAPIView):
    # queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        order_id = self.kwargs['pk']
        order = Order.objects.get(pk=order_id)
        order_items = OrderItem.objects.filter(order=order)
        return order_items


    
