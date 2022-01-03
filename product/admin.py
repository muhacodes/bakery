from django.contrib import admin
from .models import Product, Booking, Classes, Category

admin.site.register(Product)
admin.site.register(Booking)
admin.site.register(Classes)
admin.site.register(Category)