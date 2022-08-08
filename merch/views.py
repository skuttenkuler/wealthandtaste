from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
import datetime
import json
from .utils import cartData
from .models import *

def store(request):
    products = Merch.objects.all()
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

    #print(action)
    #print(productID)

    #get user and product, update orderItem
    customer = request.user.customer
    print(customer)
    product = Merch.objects.get(id=productID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

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
    

    return JsonResponse('Item was addes', safe=False)

def processOrder(request):
    #create order timestamp
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    return JsonResponse('payment complete', safe=False)