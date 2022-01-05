from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']

        content = """"
        New Email From : {}
        Email : {}
        phone : {}
        Message : {}

        """.format(name, email, phone, message)
        try:
            # send_mail(name, message, 'infomohacodes@gmail.com', ['infomohacodes@gmail.com'])
            return HttpResponse("success")
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

    context = {
        'form' : form,
    }
    return render(request, 'frontend/contact-us.html', context)


def sendemail(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():

        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        
        
        content = """"
            New Email From : {}
            Email : {}
            phone : {}
            Message : {}

            """.format(name, email, phone, message)

        my_dict = {"message":[],};
        try:
            send_mail(name, content, 'infomohacodes@gmail.com', ['infomohacodes@gmail.com'])
            my_dict["message"].append(1)
        except BadHeaderError:
            my_dict["message"].append(0)

        return JsonResponse(my_dict)
    return JsonResponse({'message': 'form is not valid'})


def about(request):
    return render(request, 'frontend/about.html')


def confirm(request):
    
    return render(request, 'frontend/confirmation.html')