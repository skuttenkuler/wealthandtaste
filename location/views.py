from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Location

def index(request):
    details = Location.objects.all()
    template = loader.get_template('index.html')
    context = {
        'details': details
    }
    return HttpResponse(template.render(context,request))
