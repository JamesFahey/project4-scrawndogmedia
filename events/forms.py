from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    """Form to make a booking"""
    class Meta:
        model = Booking
        fields = ('user',
                  'name',
                  'email',
                  'event_type',
                  'event_date',
                  'event_image',
                  'info',)
        widgets = {
            'event_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control',
                                          'placeholder': 'Select a date',
                                                         'type': 'date'}),
            'info': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
                'info': ('Tell us as much as you can about your day:'),
            }


class EditForm(forms.ModelForm):
    """Form to edit a booking"""
    class Meta:
        model = Booking
        fields = ('name',
                  'email',
                  'event_type',
                  'event_date',
                  'event_image',
                  'info',)
        widgets = {
            'event_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control',
                                          'placeholder': 'Select a date',
                                                         'type': 'date'}),
            'info': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
                'info': ('Tell us as much as you can about your day:'),
            }
