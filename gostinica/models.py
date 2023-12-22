from django.db import models
from django.urls import reverse


class Room(models.Model):
    """
    Class for room model
    """
    room_number = models.IntegerField(verbose_name='Номер комнаты')
    cost_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за ночь')
    description = models.TextField(null=True, verbose_name='Описание')
    typeroom = models.ForeignKey('TypeRoom', on_delete=models.SET_NULL, null=True, verbose_name='Тип номера')
    photo = models.ImageField(upload_to="photos_rooms", default=None, blank=True, null=True, verbose_name='Фото номера')

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"
        ordering = ['room_number']

    def __str__(self):
        """
        Return string Room number
        """
        return str(self.room_number)

    # def get_absolute_url(self):
    #     return reverse('')

class TypeRoom(models.Model):
    """
    Class for typeroom model
    """
    title = models.CharField(max_length=20, verbose_name='Название')

    class Meta:
        verbose_name = "Тип комнаты"
        verbose_name_plural = "Типы комнат"

    def __str__(self):
        """
        Return string TypeRoom title
        """
        return self.title

# # Бронирование
# class Reservation(models.Model):
#     check_in_date = models.DateField()
#     check_out_date = models.DateField()
#     room = models.ForeignKey('Room', on_delete=models.CASCADE)
#     user = models.ForeignKey('User', on_delete=models.CASCADE)
#     STATUS_CHOICES = (('o','Open'),('c','Close'))
#     status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='o')
#
# # Пользователь
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
# # Отзыв
# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     comment = models.TextField()
