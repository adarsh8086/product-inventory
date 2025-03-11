

from django.urls import path
from .views import ProductList, ProductDetail, product_inventory

urlpatterns = [
    # API Endpoints
    path('api/products/', ProductList.as_view(), name='product_list'),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),

    # Frontend Endpoint for Products (Root URL)
    path('', product_inventory, name='product_inventory_home'), 
]
