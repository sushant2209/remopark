# smartparking_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('book', views.booking,name="book"),
    path('payment', views.handle_payment, name='payment'),
    path('trial/<int:parking_spot_id>/', views.parking_spot_detail),
    path('booking_success/<str:name>/<str:spots>', views.booking_success, name='booking_success'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('map/', views.map, name='map'),
    path('dyp/', views.dyp, name='dyp'),
    path('destination.html/', views.destination, name='destination'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),    
]
