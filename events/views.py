from django.shortcuts import render
from django.views import generic
from .models import Event

def home(request):
    return render(request, 'index.html')


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by("event_date")
    template_name = "event_page.html"