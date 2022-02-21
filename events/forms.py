from django import forms
from .models import Event

EventType = (
    ("WEDDING", "Wedding"),
    ("CHRISTENING", "Christening"),
    ("OTHER", "Other"),
)

class BookingForm(forms.Form):
    name = forms.CharField(label="Full Name", max_length=100)
    email = forms.EmailField(label="Email")
    event_type = forms.ChoiceField(choices=EventType)
    event_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    info = forms.CharField(label="Please tell us as much as you can about your day", max_length=500)
    


