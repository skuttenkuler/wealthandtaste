from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.views import View
import datetime
import json
from .utils import *
from .models import *

def store(request):
    products = Merch.objects.all()
    
    for p in products:
        print('--------')
        for i in p.sizes.values():
            print(i['product_id'])
        print('--------')
       
    data = cartData(request)
    cartItems = data['cartItems']
    context = {
        "cartItems": cartItems,
        "products":products
    }
    return render(request, 'merch/store.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    print("------")
    print("data: ")
    print("------")
    context= {
        'cartItems': cartItems,
        'order': order,
        'items':items
    }
    return render(request, 'merch/cart.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {
        "cartItems": cartItems,
        "order": order,
        "items":items
    }
    return render(request, 'merch/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    # sizeID = data['size']
    customer = request.user.customer
    #print(customer)
    product = Merch.objects.get(id=productID)
    size = ProductSize.objects.get(id=sizeID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product, size=size)
    print("HERE", orderItem)
    #add and remove logic
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)

    #save item 
    orderItem.save()

    #remove if 0
    if orderItem.quantity <= 0:
        orderItem.delete()
    

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    #create order timestamp
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    # print(data)
    customer, order = CustomerOrder(request, data)
    #check total matches in cart
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    print(order)
    if order.complete == True:
        #send email of order after completion
        subject = 'WEBISTE MERCH ORDER'
        name = customer
        desc = order
        form_data = {
            'name':name,
            'desc':desc
        }
        html_message = render_to_string('merchOrder.html',{'data':form_data})
        plain_message = strip_tags(html_message)
        try:
            #print(subject,html)
            email = EmailMessage(   subject,
                                    plain_message,
                                    settings.EMAIL,
                                    [settings.EMAIL]
            )
        except BadHeaderError:
            return HttpResponse("invalid header")
        return redirect("booking")
    return JsonResponse('payment complete', safe=False)
