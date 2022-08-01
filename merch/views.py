from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Merch

def store(request):
    context = {}
    return render(request, 'merch/store.html', context)

def cart(request):
    context = {}
    return render(request, 'merch/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'merch/checkout.html', context)