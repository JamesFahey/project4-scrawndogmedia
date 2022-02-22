from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Requested"), (1, "Confirmed"))

EventType = (
    ('WEDDING', 'Wedding'),
    ('CHRISTENING', 'Christening'),
    ('OTHER', 'Other'),
)

class Event(models.Model):
    """A class to represent events model."""
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    event_type = models.CharField(blank=True, choices=EventType, max_length=30, null=True)
    event_date = models.DateField(null=True)
    info = models.TextField(max_length=500, blank=True, null=True)
    event_image = CloudinaryField('image', default='placeholder', null=True)
    status = models.IntegerField(choices=STATUS, default=0, null=True)

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        return self.name