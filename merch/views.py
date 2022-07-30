from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Merch

def index(request):
    items = Merch.objects.all()
    template = loader.get_template('index.html')
    context = {
        'items': items
    }
    return HttpResponse(template.render(context,request))
