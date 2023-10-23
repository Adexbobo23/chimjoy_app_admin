from django.urls import path
from .views import carlist, carlistdark, booking, about, contact, cardetails

urlpatterns = [
    path('cars/', carlist, name='cars'),
    path('carslistdark/', carlistdark, name='dark'),
    path('booking/', booking, name='booking'),
    path('about/', about, name='about'),
    path('contact/', contact, name="contact"),
    path('vehicles/<int:vehicle_id>/', cardetails, name='car-details'),
]