from django.contrib import admin
from .models import Vehicle, RideBooking

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(RideBooking)
# admin.site.register(CarBooking)