



from rest_framework import status, generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# List all products
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Update a product
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


from django.shortcuts import render
from .models import Product

def product_inventory(request):
    products = Product.objects.all()
    return render(request, 'product_inventory.html', {'products': products})
