# Generated by Django 3.2.9 on 2021-11-25 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_cream'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cream',
        ),
    ]
