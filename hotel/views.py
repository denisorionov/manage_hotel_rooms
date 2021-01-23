from django.shortcuts import render
from rest_framework import filters, generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from hotel.models import Room, Booking
from hotel.serializers import RoomSerializer, BookingSerializer


def view_main_page(request):
    rooms = Room.objects.all()
    return render(request, template_name="index.html", context={'rooms': rooms})


class RoomApiView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'id']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'room_id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            room = Room.objects.get(pk=request.data['room_id'])
        except Room.DoesNotExist:
            return Response(f"room id {request.data['room_id']} not found", status=status.HTTP_404_NOT_FOUND)
        room.delete()
        return Response(f"room id {request.data['room_id']} deleted", status=status.HTTP_200_OK)


class BookingApiView(generics.ListAPIView):
    queryset = Booking.objects.all().order_by('date_start')
    serializer_class = BookingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['room__id']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        try:
            room = Room.objects.get(pk=request.data['room_id'])
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = Booking.objects.create(
                room=room,
                date_start=serializer.validated_data['date_start'],
                date_end=serializer.validated_data['date_end']
            )
            return Response({'booking_id': booking.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            booking = Booking.objects.get(pk=request.data['booking_id'])
        except Booking.DoesNotExist:
            return Response(f"booking id {request.data['booking_id']} not found", status=status.HTTP_404_NOT_FOUND)
        booking.delete()
        return Response(f"booking id {request.data['booking_id']} deleted", status=status.HTTP_200_OK)
