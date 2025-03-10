# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.product_list, name='product_list'),  # List of all products
#     path('add/', views.add_product, name='add_product'),  # Form to add new product
#     path('update/<int:pk>/', views.update_product, name='update_product'),  # Form to update existing product
#     path('delete/<int:pk>/', views.delete_product, name='delete_product'),  # Page to delete product



#     # for Api
#     path('api/add/', views.api_add_product, name='api_add_product'),
#     path('api/update/<int:pk>/', views.api_update_product, name='api_update_product'),
#     path('api/delete/<int:pk>/', views.api_delete_product, name='api_delete_product')
# ]

# from django.urls import path
# from .views import product_list, api_add_product, api_update_product, api_delete_product,add_product,update_product, delete_product

# urlpatterns = [
    
#     path('product_list/', product_list, name='product_list'),
#     path('add/', api_add_product, name='add_product'),
#     path('addd/', add_product, name='add_product_form'),  # Add product form (HTML page)
#     path('products/update/<int:pk>/', update_product, name='update_product'),
#     path('products/delete/<int:pk>/', delete_product, name='delete_product'),

#     # API endpoints for managing products
#     path('api/products/', api_add_product, name='api_add_product'),
#     path('api/products/<int:pk>/', api_update_product, name='api_update_product'),
#     path('api/delete/<int:pk>/', api_delete_product, name='api_delete_product'),
# ]



# from django.urls import path
# from .views import api_list_products, api_add_product, api_update_product, api_delete_product

# urlpatterns = [
#     path('api/products/', api_list_products, name='api_list_products'),
#     path('api/products/add/', api_add_product, name='api_add_product'),
#     path('api/products/<int:pk>/update/', api_update_product, name='api_update_product'),
#     path('api/products/<int:pk>/delete/', api_delete_product, name='api_delete_product'),
# ]


# from django.urls import path
# from .views import ProductList, ProductDetail, product_inventory

# urlpatterns = [
#     # API Endpoints
#     path('api/products/', ProductList.as_view(), name='product_list'),
#     path('api/products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),

#     # Frontend Endpoint
#     path('products/', product_inventory, name='product_inventory_list'),
# ]


from django.urls import path
from .views import ProductList, ProductDetail, product_inventory

urlpatterns = [
    # API Endpoints
    path('api/products/', ProductList.as_view(), name='product_list'),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),

    # Frontend Endpoint for Products (Root URL)
    path('', product_inventory, name='product_inventory_home'),  # Empty path will match the root
]
