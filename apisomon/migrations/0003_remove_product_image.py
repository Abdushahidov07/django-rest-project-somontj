# Generated by Django 4.2.16 on 2024-11-16 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apisomon', '0002_product_category_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
