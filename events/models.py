from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Requested"), (1, "Confirmed"))

class Event(models.Model):
    EventType = models.TextChoices('EventType', 'WEDDING CHRISTENING OTHER')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(blank=True, choices=EventType.choices, max_length=20)
    event_date = models.DateField()
    info = models.TextField(max_length=500)
    event_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        return self.event_type