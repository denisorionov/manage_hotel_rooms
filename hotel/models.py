from django.db import models


class Room(models.Model):
    description = models.TextField('описание', blank=True)
    price = models.DecimalField('цена', max_digits=9, decimal_places=2, db_index=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings', verbose_name='номер')
    date_start = models.DateField('дата начала', db_index=True)
    date_end = models.DateField('дата окончания брони', db_index=True)

    def __str__(self):
        return str(self.room.id)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
