from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django import forms
from django.conf import settings
from .models import Booking
from .forms import BookingForm, EditForm
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.generic import DeleteView
from cloudinary.forms import cl_init_js_callbacks


def home(request):
    return render(request, 'index.html')


class BookingList(ListView):
    """View to list all bookings"""
    model = Booking
    template_name = "event_page.html"

    """function to only show user bookings"""
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingDetails(DetailView):
    """View to show a booking in more detail"""
    model = Booking
    template_name = "booking_details.html"


class AddBooking(SuccessMessageMixin, CreateView):
    """View to create a booking """
    model = Booking
    form_class = BookingForm
    template_name = "book_event.html"
    success_message = ("Thank you for your booking! Someone will be in" +
                       "contact soon to discuss further arrangements" +
                       " and payment")
    widgets = {
            'event_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control',
                                          'placeholder': 'Select a date',
                                                         'type': 'date'}),
    }


class UpdateBooking(SuccessMessageMixin, UpdateView):
    """View to update a booking """
    model = Booking
    form_class = EditForm
    template_name = "edit_event.html"
    success_message = "You have successfully edited your booking"
    widgets = {
            'event_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control',
                                          'placeholder': 'Select a date',
                                                         'type': 'date'}),
    }


class CancelBooking(SuccessMessageMixin, DeleteView):
    """View to cancel a booking """
    model = Booking
    template_name = "cancel_event.html"
    success_message = "You have successfully cancelled your booking"
    success_url = reverse_lazy('event_page')


    """View to create a calendar"""
def event_calendar(request, year=datetime.now().year,
                   month=datetime.now().strftime('%B')):
    name = "James"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(
        year,
        month_number)

    """function to add confirmed bookings to the calendar"""
    event_list = Booking.objects.filter(
        event_date__year=year,
        event_date__month=month_number,
        status=1
    )

    return render(request, 'calendar.html', {
        'name': name,
        'year': year,
        'month': month,
        'cal': cal,
        'event_list': event_list,
        })
