from django.db import models
from config import settings


NULLABLE = {'blank': True, 'null': True}


class Nice_habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель привычки', **NULLABLE)
    action = models.CharField(max_length=100, verbose_name='действие', **NULLABLE)

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Приятная привычка'
        verbose_name_plural = 'Приятные привычки'


class Habit(models.Model):
    PERIOD_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель привычки', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место', **NULLABLE)
    time = models.TimeField(verbose_name='время', **NULLABLE)
    action = models.CharField(max_length=100, verbose_name='действие', **NULLABLE)
    related_habit = models.ForeignKey(Nice_habit, **NULLABLE, on_delete=models.SET_NULL, verbose_name='связанная привычка')
    period = models.CharField(max_length=100, choices=PERIOD_CHOICES, default=PERIOD_CHOICES[0],
                              verbose_name='Периодичность')
    reward = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    time_to_act = models.IntegerField(verbose_name='время на привычку', **NULLABLE)
    is_public = models.BooleanField(**NULLABLE, verbose_name='публичность')

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Полезная привычка'
        verbose_name_plural = 'Полезные привычки'

