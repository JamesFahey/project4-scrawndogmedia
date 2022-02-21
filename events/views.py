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
    if request.method == "POST":
        form = book(request.POST)

        if form.is_valid():
            e = form.cleaned_data["event_type"]
            t = Event(event_type=e)
            t.save()
    else:
        form = book()
    return render(request, "book_event.html", {"form":form}) 
