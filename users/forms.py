from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomUserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)


class CustomUserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


from django import forms
from .models import UserProfileAbout

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileAbout
        fields = [
            'profile_image',
            'first_name',
            'last_name',
            'about',
            'phone_number',
            'gender',
            'location',
            'email_address',
        ]


from django import forms

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()


