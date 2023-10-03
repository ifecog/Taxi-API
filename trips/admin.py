from django.contrib import admin

from .models import Trip

class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude', 'status', 'last_location_update')
    list_filter = ('status',)
    readonly_fields = ('id', 'created_time', 'updated_time')

    fieldsets = (
        ('Trip Information', {
            'fields': ('id', 'pickup_address', 'dropoff_address', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_time', 'updated_time'),
            'classes': ('collapse',)  # Hide this section by default
        }),
    )
    

admin.site.register(Trip, TripAdmin)