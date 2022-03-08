from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('user', 'name', 'email', 'event_type', 'status',
                    'created_on', 'event_date')
    search_fields = ['name', 'event_type', 'created_on']
    list_filter = ('status', 'created_on', 'event_date')
    actions = ['update_status']

    def update_status(self, request, queryset):
        queryset.update(status=1)
