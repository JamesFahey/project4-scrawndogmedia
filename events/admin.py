from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email', 'event_type', 'status', 'event_date')
    search_fields = ['name', 'event_type']
    list_filter = ('status', 'event_date')
    summernote_fields = ('info')
    actions = ['update_status']

    def update_status(self, request, queryset):
        queryset.update(status=1)
