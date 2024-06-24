from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name='Изображение',
                               help_text='Загрузите свой аватар')
    phone = models.CharField(blank=True, null=True, verbose_name='Телефон', help_text='Введите номер телефона')
    country = models.CharField(max_length=150, verbose_name='Страна')

    token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
