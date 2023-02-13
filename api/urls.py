from django.urls import path, include
from rest_framework import routers

from products.views import \
CategoryListView, \
OrderDetailView, \
OrderListView, \
OrderListView, \
ProductDetailView, \
ProductListView, \
CategoryDetailView
from users.views import UserView \


router = routers.DefaultRouter()
router.register(r'users', UserView, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='products-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
    # path('product-categories/', ProductCategoryList.as_view()),
    # path('product-categories/<int:pk>', ProductCategoryDetail.as_view()),

]