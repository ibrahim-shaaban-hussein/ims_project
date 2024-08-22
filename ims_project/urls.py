from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    # Define the root URL pattern here
    path('', include('inventory.urls')),  # Direct root URL to the inventory app
]

