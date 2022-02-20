from django.shortcuts import render
from django.views import generic
from .models import Event
from .forms import book


def home(request):
    return render(request, 'index.html')


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by("event_date")
    template_name = "event_page.html"


def Book(request):
    form = book()
    return render(request, "book_event.html", {"form":form}) 