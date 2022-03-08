from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import home, BookingList, BookingDetails, AddBooking
from .views import UpdateBooking, CancelBooking, event_calendar


# Create your tests here.


class TestUrls(TestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_event_page_url_resolves(self):
        url = reverse('event_page')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, BookingList)

    def test_booking_details_url_resolves(self):
        url = reverse('booking_details', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, BookingDetails)

    def test_book_event_url_resolves(self):
        url = reverse('Book Event')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AddBooking)

    def test_edit_event_url_resolves(self):
        url = reverse('edit_event', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UpdateBooking)

    def test_cancel_event_url_resolves(self):
        url = reverse('cancel_event', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CancelBooking)

    def test_calendar_url_resolves(self):
        url = reverse('calendar')
        print(resolve(url))
        self.assertEquals(resolve(url).func, event_calendar)
