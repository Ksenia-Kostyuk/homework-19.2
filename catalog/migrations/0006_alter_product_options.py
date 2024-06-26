# Generated by Django 4.2.2 on 2024-06-29 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_is_active"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "permissions": [
                    ("can_edit_is_active_product", "Can edit is active product"),
                    ("can_edit_description_product", "Can edit description product"),
                    ("can_edit_category_product", "Can edit category product"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
