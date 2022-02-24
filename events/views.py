from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Event
from .models import Booking
from .forms import BookingForm


def home(request):
    return render(request, 'index.html')


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by("event_date")
    template_name = "event_page.html"


def book(request):
    if request.method == "POST":
        user = request.user
        form = BookingForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            event_type = form.cleaned_data["event_type"]
            event_date = form.cleaned_data["event_date"]
            info = form.cleaned_data["info"]
            booking = Booking(name=name, email=email, event_type=event_type, event_date=event_date, info=info, user=user)
            booking.save()

        return HttpResponseRedirect('event_page/')

    else:
        form = BookingForm()
    return render(request, "book_event.html", {"form":form}) 
