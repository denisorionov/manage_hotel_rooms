from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hotel.models import Room, Booking
from hotel.serializers import RoomSerializer, BookingSerializer


def view_main_page(request):
    rooms = Room.objects.all()
    return render(request, template_name="index.html", context={'rooms': rooms})


@api_view(['GET', 'POST', 'DELETE'])
def room_api(request):
    if request.method == 'GET':
        rooms = Room.objects.all().order_by('price')
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'room_id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            room = Room.objects.get(pk=request.data['room_id'])
        except Room.DoesNotExist:
            return Response(f"room id {request.data['room_id']} not found", status=status.HTTP_404_NOT_FOUND)
        room.delete()
        return Response(f"room id {request.data['room_id']} deleted", status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def booking_api(request, pk):
    try:
        room = Room.objects.get(pk=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        bookings = room.bookings.order_by('date_start')
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        try:
            booking = Booking.objects.get(pk=request.data['booking_id'])
        except Booking.DoesNotExist:
            return Response(f"booking id {request.data['booking_id']} not found", status=status.HTTP_404_NOT_FOUND)
        booking.delete()
        return Response(f"booking id {request.data['booking_id']} deleted", status=status.HTTP_200_OK)


@api_view(['POST'])
def booking_create_api(request):
    if request.method == 'POST':
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
