# Generated by Django 3.2.9 on 2021-11-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20211126_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='timestamp',
            field=models.DateField(),
        ),
    ]
