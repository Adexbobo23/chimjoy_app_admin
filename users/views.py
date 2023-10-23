from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from application.models import Vehicle
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django import forms
from .models import UserProfileAbout
from .forms import UserProfileForm
from django.shortcuts import render
from application.models import RideBooking

User = get_user_model()

def register(request):
    class CustomUserCreationForm(UserCreationForm):
        email = forms.EmailField(max_length=254, help_text="Required. Enter a valid email address.")

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid username or password') 

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})



def home(request):
    # Fetch the first 10 vehicles
    vehicles = Vehicle.objects.all()[:10]
    
    return render(request, 'index-4.html', {'vehicles': vehicles})



def custom_logout(request):
    logout(request)
    return redirect('loginn')


@login_required(login_url='loginn')
def dashboard(request):
    # Fetch booking details for the current user
    user_bookings = RideBooking.objects.filter(user=request.user)
    return render(request, 'account-dashboard.html', {'user_bookings': user_bookings})


# @login_required(login_url='login')
# def profile(request):
#     return render(request, 'account-profile.html')

@login_required(login_url='loginn')
def profile(request):
    user_profile, created = UserProfileAbout.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        print(form.cleaned_data)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'account-profile.html', {'form': form})




@login_required(login_url='loginn')
def orders(request):
    # Fetch booking details for the current user
    user_bookings = RideBooking.objects.filter(user=request.user)
    
    return render(request, 'account-booking.html', {'user_bookings': user_bookings})


@login_required(login_url='loginn')
def favorite(request):
    return render(request, 'account-favorite.html')


def error(request):
    return render(request, '404.html')


# Password Reset

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_bytes, smart_str
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PasswordResetRequestForm

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                # Generate a token
                token = default_token_generator.make_token(user)
                # Encode the user ID
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                # Create the password reset URL
                reset_url = request.build_absolute_uri(
                    reverse('password_reset', args=[uidb64, token])
                )
                # Send a reset email with the reset URL
                send_mail(
                    'Password Reset Request',
                    f'Use the following link to reset your password: {reset_url}',
                    'admin@chimjoylogistics.com.ng',
                    [email],
                    fail_silently=False,
                )
                return redirect('password_reset_done')
            except User.DoesNotExist:
                pass
    else:
        form = PasswordResetRequestForm()
    return render(request, 'password_reset_request.html', {'form': form})


from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_bytes, smart_str
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms

class PasswordResetForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

def password_reset(request, uidb64, token):
    try:
        user = User.objects.get(pk=force_text(urlsafe_base64_decode(uidb64)))
        if default_token_generator.check_token(user, token):
            if request.method == 'POST':
                form = PasswordResetForm(request.POST)
                if form.is_valid():
                    new_password = form.cleaned_data['password']
                    user.set_password(new_password)
                    user.save()
                    login(request, user)
                    # Redirect to a success page
                    return redirect('password_reset_complete')
            else:
                form = PasswordResetForm()
            return render(request, 'password_reset_form.html', {'form': form})
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    return render(request, 'password_reset_invalid.html')
