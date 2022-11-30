from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from datetime import date

from .models import Artist,GuestArtist

def index(request):
    artists = Artist.objects.all()
    guests = GuestArtist.objects.all()

    context = {
        'artists': artists,
        'guests': guests
    }
    return render(request, 'artists/index.html', context)


def single_artist(request,id):
    artist = Artist.objects.get(id=id)
    context= {
        'artist': artist,
        'iterator':range(0,9)
    }
    return render(request, 'artists/artist.html', context)

