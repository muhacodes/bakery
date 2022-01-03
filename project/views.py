from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from backend.models import Testimonials
from product.models import Category, Product
from django.urls import reverse
from cart.cart import Cart
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
# Create your views here.

def home(request):

    # cat = Product.objects.all()
    context = {
        'Testimonials' : Testimonials.objects.all(),
        'products' : Product.objects.filter(category__special_offer = True),
    }

    return render(request, 'frontend/index.html', context)


def product_detail(request, slug):

    context = {
        'object_list' : Product.objects.get(slug=slug)
    }
    return render(request, 'frontend/product-detail.html', context)


def contact_us(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['from_email']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']

        try:
            send_mail(name, message, email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

    context = {
        'form' : form,
    }
    return render(request, 'frontend/contact-us.html', context)



def about(request):
    return render(request, 'frontend/about.html')


def confirm(request):
    
    return render(request, 'frontend/confirmation.html')