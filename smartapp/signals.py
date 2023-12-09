# # smartparking_app/signals.py
# from django.db.models.signals import post_migrate
# from django.dispatch import receiver
# from .models import ParkingSpot

# @receiver(post_migrate)
# def create_parking_slots(sender, **kwargs):
#     if sender.name == 'smartparking_app':
#         existing_slots_count = ParkingSpot.objects.count()
#         total_slots_needed = 48  # Total slots needed for a full day (24 hours * 2 slots/hour)

#         if existing_slots_count < total_slots_needed:
#             for slot_number in range(existing_slots_count + 1, total_slots_needed + 1):
#                 ParkingSpot.objects.create(spot_number=slot_number)

#         print('Parking spots created or updated successfully.')
