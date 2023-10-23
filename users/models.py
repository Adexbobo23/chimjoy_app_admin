from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

    def save_to_user_model(self):
        # Create a user instance and set its attributes
        user = User()
        user.username = self.username
        user.email = self.email
        user.set_password(self.password)
        user.save()


class UserProfileAbout(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    about = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    location = models.CharField(max_length=255, blank=True)
    email_address = models.EmailField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
