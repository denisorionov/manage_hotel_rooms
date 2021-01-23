from django.contrib import admin
from django.urls import path

from hotel.views import view_main_page, RoomApiView, BookingApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_main_page),
    path('rooms/', RoomApiView.as_view(), name='rooms'),
    path('bookings/', BookingApiView.as_view(), name='bookings'),
]
