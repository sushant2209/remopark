# smartparking_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('smartapp.urls')),  # Include app-specific URLs
    # Add other project-wide URLs as needed
]
