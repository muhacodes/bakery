# Generated by Django 3.2.9 on 2021-12-28 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_customer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0018_rename_image1_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('appartment', models.CharField(blank=True, max_length=500, null=True)),
                ('street', models.CharField(blank=True, max_length=500, null=True)),
                ('LandMark', models.CharField(blank=True, max_length=500, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField()),
                ('message', models.TextField(blank=True, max_length=1000, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('deliver', models.DateField(blank=True, null=True, verbose_name='Delivery Date')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping', to='order.address')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
