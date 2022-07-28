from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Artist

def index(request):
    artists = Artist.objects.all()
    template = loader.get_template('artists/index.html')
    context = {
        'artists': artists
    }
    return HttpResponse(template.render(context,request))
