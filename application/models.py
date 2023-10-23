from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Vehicle(models.Model):
    TRANSMISSION_CHOICES = (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    )
    
    FUEL_CHOICES = (
        ('Gasoline', 'Gasoline'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
    )

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    exterior_color = models.CharField(max_length=50)
    interior_color = models.CharField(max_length=50)
    door = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=15)
    daily_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    vehicle_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_CHOICES, default='Automatic')
    
    passenger_capacity = models.PositiveSmallIntegerField()
    
    luggage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])
    
    fuel_type = models.CharField(max_length=50, choices=FUEL_CHOICES)
    
    registration_number = models.CharField(max_length=50)
    
    car_picture_main = models.ImageField(upload_to='vehicles/')
    other_car_picture_one = models.ImageField(upload_to='vehicles/')
    other_car_picture_two = models.ImageField(upload_to='vehicles/')
    other_car_picture_three = models.ImageField(upload_to='vehicles/')
    other_car_picture_four = models.ImageField(upload_to='vehicles/')
    
    description = models.TextField(default='Describe the car')
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class RideBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=100, default='select car model')
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    
    # Add email and phone number fields
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Ride from {self.pickup_location} to {self.destination} on {self.date} at {self.time}"


class CarBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=100, default='select car model')
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    
    # Add email and phone number fields
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Ride from {self.pickup_location} to {self.destination} on {self.date} at {self.time}"
