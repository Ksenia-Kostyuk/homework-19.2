from django.db import models

from users.models import User


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    price = models.PositiveIntegerField(verbose_name='Цена')
    created_at = models.DateField(null=True, verbose_name='Дата создания')
    updated_at = models.DateField(null=True, verbose_name='Дата последнего изменения')

    owner = models.ForeignKey(User, verbose_name='Владелец',blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} - {self.description}. Цена: {self.price}'


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Продукт')
    num_version = models.PositiveIntegerField(verbose_name='Номер версии')
    name_version = models.CharField(max_length=100, verbose_name='Наименование')
    is_active = models.BooleanField(default=True, verbose_name="Признак текущей версии")

    def __str__(self):
        return f'{self.name_version} - {self.num_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
