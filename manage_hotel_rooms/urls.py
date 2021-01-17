from django.contrib import admin
from django.urls import path

from hotel.views import view_main_page, room_api, booking_api, booking_create_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_main_page),
    path('rooms/', room_api),
    path('room/id=<int:pk>/bookings/', booking_api),
    path('booking/create/', booking_create_api)
]
