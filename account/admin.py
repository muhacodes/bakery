from django.contrib import admin
from .models import User, Shipping, customer
# Register your models here.

admin.site.register(User)
admin.site.register(Shipping)
admin.site.register(customer)