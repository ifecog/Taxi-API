from django.contrib import admin

from .models import Trip

# Register your models here.
# class TripAdmin(admin.ModelAdmin):
#     fields = (
#         'id', 'pick_up_address', 'drop_off_address', 'status', 'created', 'updated',
#     )
#     list_display = (
#         'id', 'pick_up_address', 'drop_off_address', 'status', 'created', 'updated',
#     )
#     list_filter = (
#         'status',
#     )
#     readonly_fields = (
#         'id', 'created', 'updated',

class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'pickup_address', 'dropoff_address', 'status', 'created_time', 'updated_time')
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