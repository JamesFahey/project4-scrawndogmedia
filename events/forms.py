from .models import Event
from django import forms


# EventType = (
#     ("WEDDING", "Wedding"),
#     ("CHRISTENING", "Christening"),
#     ("OTHER", "Other"),
# )

# class BookingForm(forms.Form):
#     name = forms.CharField(label="Full Name", max_length=100)
#     email = forms.EmailField(label="Email")
#     event_type = forms.ChoiceField(choices=EventType)
#     event_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
#     info = forms.CharField(label="Please tell us as much as you can about your day", max_length=500)
    
class BookingForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name',
            'email',
            'event_type',
            'event_date',
            'info',)
        widgets = {
            'event_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'info': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
                'info': ('Tell us as much as you can about your day:'),
            }


