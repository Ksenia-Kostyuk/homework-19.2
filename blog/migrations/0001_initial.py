# Generated by Django 5.0.4 on 2024-05-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MyBlog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Заголовок")),
                (
                    "slug",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Понятное описание"
                    ),
                ),
                (
                    "content",
                    models.TextField(blank=True, null=True, verbose_name="Содержимое"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "date_create",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "publication_sign",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Признак публикации",
                    ),
                ),
                (
                    "views",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Просмотры"
                    ),
                ),
            ],
            options={
                "verbose_name": "Заголовок",
                "verbose_name_plural": "Заголовки",
            },
        ),
    ]
