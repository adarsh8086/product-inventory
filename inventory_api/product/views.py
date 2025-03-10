# from django.shortcuts import render, redirect
# from .models import Product
# from .forms import ProductForm  # We'll use a Django form to handle the add/update operations

# # Display all products
# def product_list(request):
#     products = Product.objects.all()  # Get all products
#     return render(request, 'product_list.html', {'products': products})

# # Add a new product (form submission)
# def add_product(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new product to the database
#             return redirect('product_list')  # Redirect to the product list page after adding

#     form = ProductForm()  # Empty form for new product
#     return render(request, 'add_product.html', {'form': form})

# # Update an existing product (form submission)
# def update_product(request, pk):
#     product = Product.objects.get(id=pk)  # Get the product by its ID
#     if request.method == "POST":
#         form = ProductForm(request.POST, instance=product)  # Fill the form with existing product data
#         if form.is_valid():
#             form.save()  # Save the updated product
#             return redirect('product_list')  # Redirect to the product list after update

#     form = ProductForm(instance=product)  # Fill the form with existing product data
#     return render(request, 'update_product.html', {'form': form})

# # Delete a product
# def delete_product(request, pk):
#     product = Product.objects.get(id=pk)  # Get the product by its ID
#     if request.method == "POST":
#         product.delete()  # Delete the product
#         return redirect('product_list')  # Redirect to the product list after deletion
#     return render(request, 'delete_product.html', {'product': product})





# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Product
# from .forms import ProductForm

# # Display all products (for non-AJAX calls)
# def product_list(request):
#     products = Product.objects.all()  # Get all products
#     return render(request, 'product_list.html', {'products': products})

# # Add a new product (for non-AJAX calls)
# def add_product(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new product to the database
#             return redirect('product_list')  # Redirect to the product list page after adding
#     form = ProductForm()  # Empty form for new product
#     return render(request, 'add_product.html', {'form': form})

# # Add a new product (AJAX)
# @csrf_exempt
# def api_add_product(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         stock = request.POST.get('stock')

#         if price < 0:  # Price validation
#             return JsonResponse({'error': 'Price cannot be negative'}, status=400)

#         product = Product.objects.create(name=name, price=price, stock=stock)
#         return JsonResponse({'success': 'Product added successfully', 'id': product.id})

# # Update an existing product (for non-AJAX calls)
# def update_product(request, pk):
#     product = Product.objects.get(id=pk)  # Get the product by its ID
#     if request.method == "POST":
#         form = ProductForm(request.POST, instance=product)  # Fill the form with existing product data
#         if form.is_valid():
#             form.save()  # Save the updated product
#             return redirect('product_list')  # Redirect to the product list after update
#     form = ProductForm(instance=product)  # Fill the form with existing product data
#     return render(request, 'update_product.html', {'form': form})

# # Update an existing product (AJAX)
# @csrf_exempt
# def api_update_product(request, pk):
#     try:
#         product = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         return JsonResponse({'error': 'Product not found'}, status=404)

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         stock = request.POST.get('stock')

#         if price < 0:  # Price validation
#             return JsonResponse({'error': 'Price cannot be negative'}, status=400)

#         product.name = name
#         product.price = price
#         product.stock = stock
#         product.save()

#         return JsonResponse({'success': 'Product updated successfully'})

# # Delete a product (for non-AJAX calls)
# def delete_product(request, pk):
#     product = Product.objects.get(id=pk)  # Get the product by its ID
#     if request.method == "POST":
#         product.delete()  # Delete the product
#         return redirect('product_list')  # Redirect to the product list after deletion
#     return render(request, 'delete_product.html', {'product': product})

# # Delete a product (AJAX)
# @csrf_exempt
# def api_delete_product(request, pk):
#     try:
#         product = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         return JsonResponse({'error': 'Product not found'}, status=404)

#     if request.method == 'POST':
#         product.delete()
#         return JsonResponse({'success': 'Product deleted successfully'})



# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from .models import Product
# from .serializers import ProductSerializer

# # API view to list all products and create a new product
# class ProductListView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# # API view to retrieve, update or delete a product
# class ProductDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# # API for adding a product (POST request)
# @api_view(['POST'])
# def api_add_product(request):
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success": "Product added successfully", "id": serializer.data['id']}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # API for updating a product (PUT request)
# @api_view(['PUT'])
# def api_update_product(request, pk):
#     try:
#         product = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'success': 'Product updated successfully'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # API for deleting a product (DELETE request)
# @api_view(['DELETE'])
# def api_delete_product(request, pk):
#     try:
#         product = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'DELETE':
#         product.delete()
#         return Response({'success': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)




# from django.shortcuts import render
# from .models import Product
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# List all products
# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product_list.html', {'products': products})

# # Add a product
# @api_view(['POST'])
# def api_add_product(request):
#     if request.method == 'POST':
#         # Validate and save product
#         name = request.data.get('name')
#         price = request.data.get('price')
#         product = Product.objects.create(name=name, price=price)
#         return Response({"message": "Product added", "product": {"id": product.id}}, status=status.HTTP_201_CREATED)

# # Update product
# @api_view(['POST'])
# def api_update_product(request, pk):
#     try:
#         product = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
#     name = request.data.get('name')
#     price = request.data.get('price')
#     product.name = name
#     product.price = price
#     product.save()
#     return Response({"message": "Product updated"}, status=status.HTTP_200_OK)

# # Delete product
# @api_view(['POST'])
# def api_delete_product(request, pk):
#     try:
#         product = Product.objects.get(id=pk)
#         product.delete()
#         return Response({"message": "Product deleted"}, status=status.HTTP_200_OK)
#     except Product.DoesNotExist:
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


# views.py
# from django.shortcuts import render,redirect
# from .models import Product

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product_list.html', {'products': products})

# def add_product(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         stock = request.POST.get('stock')

#         # Create and save the new product
#         product = Product.objects.create(name=name, price=price, stock=stock)
        
#         return redirect('product_list')  # Redirect to product list after adding the product

#     return render(request, 'add_product.html')  


# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import JsonResponse
# from .models import Product

# Render the product update page and handle form submission
# def update_product(request, pk):
#     # Fetch the product to be updated
#     product = get_object_or_404(Product, pk=pk)

#     if request.method == 'POST':
#         # Update the product details
#         name = request.POST.get('name')
#         price = request.POST.get('price')

#         product.name = name
#         product.price = price
#         product.save()

#         # Redirect to product list or return a success message
#         return redirect('product_list')

#     # Render the form with product data to update
#     return render(request, 'update_product.html', {'product': product})


# def delete_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)

#     if request.method == 'POST':
#         product.delete()  # Delete the product
#         return redirect('product_list')  # Redirect to the product list page

#     return render(request, 'delete_product.html', {'product': product})





# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Product
# from .serializers import ProductSerializer


# #  1. List All Products
# @api_view(['GET'])
# def api_list_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response({"products": serializer.data}, status=status.HTTP_200_OK)


# #  2. Add New Product
# @api_view(['POST'])
# def api_add_product(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Product added successfully"}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #  3. Update Product
# @api_view(['POST', 'PUT'])  # Allow both POST and PUT for flexibility
# def api_update_product(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     serializer = ProductSerializer(product, data=request.data, partial=True)
    
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Product updated successfully"}, status=status.HTTP_200_OK)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #  4. Delete Product
# @api_view(['DELETE'])
# def api_delete_product(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     product.delete()
#     return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)





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
