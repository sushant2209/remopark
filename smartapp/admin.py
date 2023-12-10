# admin.py
from django.contrib import admin
from .models import CustomUser,ParkingCenter,ParkingSpot,ContactMessage

admin.site.register(CustomUser)
admin.site.register(ParkingSpot)
admin.site.register(ContactMessage)
admin.site.register(ParkingCenter)
