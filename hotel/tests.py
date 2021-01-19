from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from hotel.models import Room, Booking


class ApiTests(APITestCase):
    def setUp(self):
        self.room = Room.objects.create(
            description='Single',
            price='5000.00'
        )
        self.booking = Booking.objects.create(
            room=self.room,
            date_start='2021-01-22',
            date_end='2021-01-24'
        )

    def tearDown(self):
        self.room.delete()

    def test_post_create_room(self):
        url = reverse('rooms')
        data = {'description': 'Dorm', 'price': '2000.00'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Room.objects.count(), 2)
        self.assertEqual(Room.objects.get(description='Dorm').price, 2000.00)

    def test_get_room(self):
        url = reverse('rooms')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Room.objects.count(), 1)
        self.assertEqual(Room.objects.get(description='Single').price, 5000.00)

    def test_delete_room(self):
        Room.objects.get().delete()
        self.assertEqual(Room.objects.count(), 0)
