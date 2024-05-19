from django.db import models

from user.models import User

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    action = models.CharField(max_length=300, verbose_name='Действие')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=250, help_text='Где выполнять привычку?', verbose_name='Место')
    time = models.DateTimeField(help_text='В какое время выполнять привычку?', verbose_name='Время выполнения')
    is_pleasant = models.BooleanField(default=False, help_text='Это приятная привычка?',
                                      verbose_name='Признак приятной привычки')
    frequency = models.IntegerField(default=1, help_text='Действие совершать один раз в N дней',
                                    verbose_name='Периодичность')
    linked_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Связанная привычка')
    reward = models.CharField(max_length=300, verbose_name='Вознаграждение')
    action_time = models.IntegerField(help_text='Укажите время на выполнение привычки в минутах',
                                      verbose_name='Время на выполнение')
    is_published = models.BooleanField(default=False, help_text='Привычку опубликовать?',
                                       verbose_name='Признак публикации')
