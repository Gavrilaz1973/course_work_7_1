from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    # username = models.CharField(max_length=50, verbose_name='имя', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    telegram_id = models.CharField(max_length=255, verbose_name='Telegram ID', **NULLABLE)

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

