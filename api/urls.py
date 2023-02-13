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
from reviews.views import ReviewsView
from users.views import UserView

user_router = routers.DefaultRouter()
user_router.register(r'users', UserView, basename='user')

review_router = routers.DefaultRouter()
review_router.register(r'reviews', ReviewsView, basename='review')

urlpatterns = [
    path('', include(user_router.urls)),
    path('', include(review_router.urls)),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='products-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
    # path('product-categories/', ProductCategoryList.as_view()),
    # path('product-categories/<int:pk>', ProductCategoryDetail.as_view()),

]