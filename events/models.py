from django.db import models
from cloudinary.models import CloudinaryField
# from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

STATUS = ((0, "Requested"), (1, "Confirmed"))

EventType = (
    ('WEDDING', 'Wedding'),
    ('CHRISTENING', 'Christening'),
    ('FAMILY SHOOTS', 'Family Shoots'),
    ('COUPLE SHOOTS', 'Couple Shoots'),
    ('PERSONAL SHOOTS', 'Personal Shoots'),
    ('OTHER', 'Other'),
)


class Event(models.Model):
    """A class to represent events model."""
    event_type = models.CharField(blank=True,
                                  choices=EventType, max_length=30, null=True)
    event_image = CloudinaryField('image', default='placeholder', null=True)

    def __str__(self):
        return f'{self.event_type}'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="booking", null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    event_type = models.CharField(blank=True, choices=EventType,
                                  max_length=30, null=True)
    event_date = models.DateField(null=True)
    event_image = CloudinaryField('image', default='placeholder', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    info = models.TextField(max_length=500, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0, null=True)

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('event_page')


class Edit(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE,
                                related_name="edit", null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    event_type = models.CharField(blank=True, choices=EventType,
                                  max_length=30, null=True)
    event_date = models.DateField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    info = models.TextField(max_length=500, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0, null=True)

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        return f'{self.name}'
