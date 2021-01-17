from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from hotel.models import Booking, Room


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'date_start', 'date_end']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'description', 'price']
