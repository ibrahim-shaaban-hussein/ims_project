# inventory/urls.py

from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.home, name='home'),  # Map the root URL to the home view
    path('product_list/', views.product_list, name='product_list'),  # List of products
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # Product detail
    path('product/create/', views.product_create, name='product_create'),  # Create product
    path('product/<int:pk>/update/', views.product_update, name='product_update'),  # Update product
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),  # Delete product
]

