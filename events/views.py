import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django import forms
from django.conf import settings
from .models import Booking
from .forms import BookingForm, EditForm





def home(request):
    return render(request, 'index.html')


class BookingList(ListView):
    model = Booking
    # queryset = Booking.objects.order_by("event_date")
    template_name = "event_page.html"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingDetails(DetailView):
    model = Booking
    template_name = "booking_details.html"

class AddBooking(SuccessMessageMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "book_event.html"
    success_message = "Thank you for your booking! Someone will be in contact soon to discuss further arrangements and payment"
    # fields = ['user',
    #         'name',
    #         'email',
    #         'event_type',
    #         'event_date',
    #         'info',
    # ]
    widgets = {
            'event_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }


# def book(request):
#     if request.method == "POST":
#         user = request.user
#         form = BookingForm(request.POST)

#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             email = form.cleaned_data["email"]
#             event_type = form.cleaned_data["event_type"]
#             event_date = form.cleaned_data["event_date"]
#             info = form.cleaned_data["info"]
#             booking = Booking(name=name, email=email, event_type=event_type, event_date=event_date, info=info, user=user)
#             booking.save()

#         return HttpResponseRedirect('event_page/')

#     else:
#         form = BookingForm()
#     return render(request, "book_event.html", {"form":form}) 

# def edit(request):
#     if request.method == "POST":
#         user = request.user
#         form = EditForm(request.POST, instance=request.user)

#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             email = form.cleaned_data["email"]
#             event_type = form.cleaned_data["event_type"]
#             event_date = form.cleaned_data["event_date"]
#             info = form.cleaned_data["info"]
#             booking = Booking(name=name, email=email, event_type=event_type, event_date=event_date, info=info, user=user)
#             booking.save()

#         return HttpResponseRedirect('event_page/')

#     else:
#         form = EditForm()
#     return render(request, "edit_event.html", {"form":form})

class UpdateBooking(SuccessMessageMixin, UpdateView):
    model = Booking
    form_class = EditForm
    template_name = "edit_event.html"
    success_message = "You have successfully edited your booking"
    # fields = [
    #     'name',
    #     'email',
    #     'event_type',
    #     'event_date',
    #     'info',
    # ]
    widgets = {
            'event_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }


class CancelBooking(SuccessMessageMixin, DeleteView):
    model = Booking
    template_name = "cancel_event.html"
    success_message = "You have successfully cancelled your booking"
    success_url = reverse_lazy('event_page')
    

def contact(request):
    if request.method == "POST":
        message_name = request.POST.get('message_name')
        message_email = request.POST.get('message_email')
        # phone = request.POST['phone']
        message = request.POST.get('message')
        send_mail(
            message_name,
            settings.EMAIL_HOST_USER,
            message,
            [message_email],
        )

        return render(request, 'home', {'name': message_name})

    else:
        return render(request, 'home', {})

def event_calendar(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "James"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(
        year,
        month_number)

    event_list = Booking.objects.filter(
        event_date__year = year,
        event_date__month = month_number,
        status = 1
    )

    return render(request, 'calendar.html', {
        'name': name,
        'year': year,
        'month': month,
        'cal': cal,
        'event_list': event_list,
        })
