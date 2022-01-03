# Generated by Django 3.2.9 on 2021-11-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_category_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='MOQ',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Minimum Order Quantity'),
        ),
        migrations.AddField(
            model_name='product',
            name='expire',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='about',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingridients',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
