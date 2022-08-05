from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse

from .models import *

def store(request):
    products = Merch.objects.all()
    context = {
        "products": products
    }
    return render(request, 'merch/store.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {
        "items":items,
        "order": order
    }
    return render(request, 'merch/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {
        "items":items,
        "order": order
    }
    return render(request, 'merch/checkout.html', context)

def updateItem(request):
    return JsonResponse('Item was addes', safe=False)