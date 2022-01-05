from django.core.checks import messages
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import addressForm, customerAdd
from account.models import customer
from .models import Address, Order, OrderItem
from product.models import Product
from cart.cart import Cart
from django.core.mail import send_mail, BadHeaderError
# Create your views here.

def checkout(request):
    addressforms = addressForm(request.POST or None)
    customerForm = customerAdd(request.POST or None)
    if request.method =='POST':

        #  some variable names
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone_number']
        
        customerobj = customer.objects.create(
            email = email,
            name = name,
            phone_number = phone
        )
        customerobj.save()
        customerinstance = customer.objects.get(id=customerobj.id)
        addressobj = Address(
            address=request.POST['address'],
            appartment=request.POST['appartment'],
            street=request.POST['street'],
            LandMark=request.POST['LandMark']
        )
        
        addressobj.save()

        cart = request.session['cart']
        mylist = []
        for key, value in cart.items():
            id = value['product_id']
            product_instance = Product.objects.get(id=id)
            mylist.append(product_instance.id)
            order_item = OrderItem.objects.create(
                product = product_instance,
                quantity= value['quantity'],
                price=value['price'],
            
            )
            order_item.save()
        
        # myorder = Order(
        #         message= request.POST['notes'],
        #     )
        myorder = Order.objects.create(
            customer = customerinstance,
            message = request.POST['notes'],
        )
        
        # print(mylist)
        for x in mylist:
           myorder.item.add(OrderItem.objects.get(id=x))
         
        # print(mylist)
        cart = Cart(request)
        cart.clear()
        sendemailsystem(name, 2654,  email, phone)
        sendUserEmail(name, 254, email)
        return HttpResponseRedirect(reverse('confirm'))
        
        return HttpResponse("end point reached")
    

    context = {
        'address' : addressforms,
        'customer' : customerForm,
    }

    return render(request, 'frontend/checkout.html', context)


def check(request):
    cart = request.session['cart']
    mycart = cart.items()
    for key, value in mycart:
        print(value["quantity"])


    return HttpResponse(cart)



def sendemailsystem(name, order_code, email, phone):
    content = """
            {} has placed an order:
            Email : {}
            Order Code : {}
            Phone : {}
            Check website for more information about the order

            """.format(name,email, order_code, phone,)
    try:
        msg = send_mail('Order has been placed', content, 'infomohacodes@gmail.com', ['infomohacodes@gmail.com'])
        return msg
    except BadHeaderError:
        return 'error'



def sendUserEmail(name, order_code, email ):
    content = """
            {} You have succesfully placed an order with us, sit back and Relax while we process your order!!:
            Order ID: : {}
            

            """.format(name, order_code,)
    try:
        msg = send_mail('Order has been placed', content, 'infomohacodes@gmail.com', [email])
        return msg
    except BadHeaderError:
        return 'error'