# smartparking_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list,name=''),
    path('book', views.booking,name="book"),
    path('trial/<int:parking_spot_id>/', views.parking_spot_detail),
    path('booking_success/<str:name>/<str:spots>', views.booking_success, name='booking_success'),
    path('payment', views.handle_payment, name='payment'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('map/', views.map, name='map'),
    path('dyp/', views.dyp, name='dyp'),
     
]
