from django import forms
from .models import RideBooking, Vehicle, CarBooking
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# List of states in Nigeria
# nigerian_states = [
#     "Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue",
#     "Borno", "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "FCT",
#     "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi",
#     "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo",
#     "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"
# ]
nigerian_states = [
    "Owerri",
    "Okigwe",
    "Orlu",
    "Oguta",
    "Izombe",
    "Umu Oma",
    "Abajah",
    "Aboh-Mbaise",
    "Nwangele",
    "Amaifeke",
    "Umuchima",
    "Anara",
    "Ahiara",
    "Emekeobibi",
    "Amike",
    "Iho",
    "Awo-Omamma",
    "Awaka",
    "Okwele",
    "Arondizuogu",
    "Nnarambia",
    "Mbieri",
    "Umuaka",
    "Ihiagwa",
    "Owerri North",
    "Umuagwo",
    "Owerri West",
    "Orodo",
    "Amakohia",
    "Ideato South",
    "Isiala Mbano",
    "Ohoba",
    "Akabo",
    "Ubomiri",
    "Amaimo",
    "Amatta",
    "Umueshi",
    "Ekwereazu",
    "Agbala",
    "Emii",
    "Ozara",
    "Umunoha",
    "Ikeduru",
    "Nkwerre",
    "Obinze",
    "Ideato North",
    "Ihitte-Uboma",
    "Ngor-Okpala",
    "Ehime - Mbano",
    "Umunumo",
    "Dikenafai"
]


class RideBookingForm(forms.ModelForm):
    pickup_location = forms.ChoiceField(choices=[(state, state) for state in nigerian_states])
    destination = forms.ChoiceField(choices=[(state, state) for state in nigerian_states])
    model = forms.ModelChoiceField(queryset=Vehicle.objects.all(), empty_label="Select a vehicle")

    class Meta:
        model = RideBooking
        fields = ['model','pickup_location', 'destination', 'date', 'time', 'email', 'phone_number']

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
    )



class CarBookingForm(forms.ModelForm):
    pickup_location = forms.ChoiceField(choices=[(state, state) for state in nigerian_states])
    destination = forms.ChoiceField(choices=[(state, state) for state in nigerian_states])
    model = forms.ModelChoiceField(queryset=Vehicle.objects.all(), empty_label="Select a vehicle")

    class Meta:
        model = RideBooking
        fields = ['model','pickup_location', 'destination', 'date', 'time', 'email', 'phone_number']

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
            return email
        except ValidationError:
            raise forms.ValidationError("Please enter a valid email address.")

