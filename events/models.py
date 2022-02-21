from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Requested"), (1, "Confirmed"))

class Event(models.Model):
    """A class to represent events model."""
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(default='jon@gmail.com', null=True)
    EventType = models.TextChoices('EventType', 'WEDDING CHRISTENING OTHER',)
    event_type = models.CharField(blank=True, choices=EventType.choices, max_length=20, null=True)
    event_date = models.DateField(null=True)
    info = models.TextField(max_length=500, null=True)
    event_image = CloudinaryField('image', default='placeholder', null=True)
    status = models.IntegerField(choices=STATUS, default=0, null=True)

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        return self.name