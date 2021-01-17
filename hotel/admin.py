from django.contrib import admin

from hotel.models import Room, Booking


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0
    fields = ['date_start', 'date_end']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [BookingInline]
    list_display = ['id', 'description', 'price']
    list_display_links = ['id', 'description']



