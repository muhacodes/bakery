from django.forms import ModelForm
from product.models  import Category, Product
from order.models import Order
from django import forms    
from account.models import customer
from .models import Address    

class addressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ('customer',)

    def __init__(self, *args, **kwargs):
        super(addressForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                # 'style': 'color: white'
        })


class customerAdd(ModelForm):
    class Meta:
        model = customer
        fields = ('name', 'email', 'phone_number',)

    def __init__(self, *args, **kwargs):
        super(customerAdd, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                # 'style': 'color: white'
        })
