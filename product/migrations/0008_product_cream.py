# Generated by Django 3.2.9 on 2021-11-25 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cream',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
