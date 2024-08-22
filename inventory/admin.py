# inventory/admin.py

from django.contrib import admin
from .models_product import ProductDetail  # or Product if you didn't rename it

admin.site.register(ProductDetail)  # or Product if you didn't rename it

