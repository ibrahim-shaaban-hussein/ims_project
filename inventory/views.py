# inventory/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product  # Ensure you have a Product model
from .forms import ProductForm  # Ensure you have a ProductForm

def home(request):
    """
    A simple view to render the home page of the inventory app.
    """
    return HttpResponse("Welcome to the Inventory Home Page!")

def product_list(request):
    """
    A view to render a list of products.
    """
    products = Product.objects.all()  # Get all products from the database
    return render(request, 'inventory/product_list.html', {'products': products})

def product_detail(request, pk):
    """
    A view to render details of a single product.
    """
    product = get_object_or_404(Product, pk=pk)  # Get product by primary key
    return render(request, 'inventory/product_detail.html', {'product': product})

def product_create(request):
    """
    A view to create a new product.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form})

def product_update(request, pk):
    """
    A view to update an existing product.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory:product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/product_form.html', {'form': form})

def product_delete(request, pk):
    """
    A view to delete a product.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('inventory:product_list')
    return render(request, 'inventory/product_confirm_delete.html', {'product': product})

