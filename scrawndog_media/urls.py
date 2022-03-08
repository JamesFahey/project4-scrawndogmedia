"""scrawndog_media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from events.views import home
from events import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path('summernote/', include('django_summernote.urls')),
    path('event_page/', views.BookingList.as_view(), name='event_page'),
    path('booking_details/<int:pk>',
         views.BookingDetails.as_view(), name='booking_details'),
    path('book_event/', views.AddBooking.as_view(), name='Book Event'),
    path('accounts/', include('allauth.urls')),
    path('booking_details/edit/<int:pk>',
         views.UpdateBooking.as_view(), name='edit_event'),
    path('booking_details/<int:pk>/cancel',
         views.CancelBooking.as_view(), name='cancel_event'),
    path("calendar/", views.event_calendar, name="calendar"),
    path("<int:year>/<str:month>/", views.event_calendar, name="calendar"),
]
