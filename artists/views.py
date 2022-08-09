from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Artist

def index(request):
    artists = Artist.objects.all()
    context = {
        'artists': artists
    }
    return render(request, 'artists/index.html', context)


def single_artist(request,id):
    artist = Artist.objects.get(id=id)
   
    context= {
        'artist': artist
    }
    return render(request, 'artists/artist.html', context)
