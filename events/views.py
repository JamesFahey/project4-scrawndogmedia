from django.shortcuts import render
from django.views import generic
from .models import Event
from .forms import BookingForm


def home(request):
    return render(request, 'index.html')


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by("event_date")
    template_name = "event_page.html"


def book(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            booking = Event(name=n)
            booking.save()

    else:
        form = BookingForm()
    return render(request, "book_event.html", {"form":form}) 
