# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class ParkingCenter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ParkingSpot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    center = models.CharField(max_length=100)
    available = models.CharField(max_length=20)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_available_slots(self):
        return [int(slot) for slot in self.available.split()]

    def get_time_slots(self):
        time_slots = {1: '11:00 AM - 11:30 AM', 2: '11:30 AM - 12:00 PM', 3: '12:00 PM - 12:30 PM'}
        return time_slots

   
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    car_no = models.CharField(max_length=20)
    slot_booked = models.CharField(max_length=10, blank=True, null=True)
    slot_booked_time = models.CharField(max_length=50, blank=True, null=True)
    location=models.CharField(max_length=100)
    center=models.CharField(max_length=100)

    def __str__(self):
        return self.username
    def __str__(self):
        return self.username

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.subject


