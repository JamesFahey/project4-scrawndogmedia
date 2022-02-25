from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm


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

class AddBooking(CreateView):
    model = Booking
    template_name = "book_event.html"
    fields = ['user',
            'name',
            'email',
            'event_type',
            'event_date',
            'info',
    ]


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

class UpdateBooking(UpdateView):
    model = Booking
    template_name = "edit_event.html"
    fields = [
        'name',
        'email',
        'event_type',
        'event_date',
        'info',
    ]