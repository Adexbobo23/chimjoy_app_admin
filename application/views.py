from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Vehicle
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from .forms import RideBookingForm, CarBookingForm

# Create your views here.

def carlist(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'cars.html', {'vehicles': vehicles})


def carlistdark(request):
    vehicles = Vehicle.objects.all()
    return render(request, '02_dark-cars.html', {'vehicles': vehicles})


@login_required(login_url='loginn')
def cardetails(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    form = RideBookingForm()

    if request.method == 'POST':
        form = RideBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful!')

            # Send an email notification to the admin
            subject = 'New Car Renting Notification'
            message = f'A new booking has been made by {request.user.username}.\n\n'
            message += f'Pickup Location: {booking.pickup_location}\n'
            message += f'Destination: {booking.destination}\n'
            message += f'Model: {booking.model}\n'
            message += f'Date: {booking.date}\n'
            message += f'Time: {booking.time}\n'
            message += f'Email: {booking.email}\n'
            message += f'Phone Number: {booking.phone_number}\n'
            message += f'Kindly reach out to this customer on {booking.phone_number} to confirm their order\n'

            from_email = 'admin@chimjoylogistics.com.ng' 
            recipient_list = ['admin@chimjoylogistics.com.ng', 'oliyideadeoluwajohn1@gmail.com']

             # Send an email to the user
            user_subject = 'Your Car Booking Details'
            user_message = 'Thank you for booking with us. Here are your booking details:\n\n'
            user_message += f'Pickup Location: {booking.pickup_location}\n'
            user_message += f'Destination: {booking.destination}\n'
            user_message += f'Model: {booking.model}\n'
            user_message += f'Date: {booking.date}\n'
            user_message += f'Time: {booking.time}\n'
            user_message += f'Email: {booking.email}\n'
            user_message += f'Phone Number: {booking.phone_number}\n'
            user_message += f'One of our Agents will reach out shortly, to confirm your order.\n'
            user_message += f'Regards \n'
            user_email = [booking.email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
            send_mail(user_subject, user_message, from_email, user_email, fail_silently=True)

            return redirect('dashboard')

    return render(request, 'car-single.html', {'vehicle': vehicle, 'form': form})



from django.core.mail import send_mail

@login_required(login_url='loginn')
def booking(request):
    vehicle = Vehicle.objects.all()
    form = CarBookingForm()

    if request.method == 'POST':
        form = CarBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful!')
            print(f"User's Email: {booking.email}")

            # Send an email notification to the admin
            subject = 'New Car Booking Notification'
            message = f'A new booking has been made by {request.user.username}.\n\n'
            message += f'Pickup Location: {booking.pickup_location}\n'
            message += f'Destination: {booking.destination}\n'
            message += f'Model: {booking.model}\n'
            message += f'Date: {booking.date}\n'
            message += f'Time: {booking.time}\n'
            message += f'Email: {booking.email}\n'
            message += f'Phone Number: {booking.phone_number}\n'
            message += f'Kindly reach out to this customer on {booking.phone_number} to confirm their order\n'

            from_email = 'admin@chimjoylogistics.com.ng' 
            recipient_list = ['admin@chimjoylogistics.com.ng', 'oliyideadeoluwajohn1@gmail.com']

            # Send an email to the user
            user_subject = 'Your Car Booking Details'
            user_message = 'Thank you for booking with us. Here are your booking details:\n\n'
            user_message += f'Pickup Location: {booking.pickup_location}\n'
            user_message += f'Destination: {booking.destination}\n'
            user_message += f'Model: {booking.model}\n'
            user_message += f'Date: {booking.date}\n'
            user_message += f'Time: {booking.time}\n'
            user_message += f'Email: {booking.email}\n'
            user_message += f'Phone Number: {booking.phone_number}\n'
            user_email = [booking.email]  # Use the user's email

            # Send both emails
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
            send_mail(user_subject, user_message, from_email, user_email, fail_silently=True)

            return redirect('dashboard')

    return render(request, 'booking.html', {'vehicle': vehicle, 'form': form})



def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')