from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from artists.models import Artist, GuestArtist
from location.models import Location


def index(request):
    artists = Artist.objects.all()
    guests = GuestArtist.objects.all()
    location = Location.objects.all()
    context = {
        'artists': artists,
        'guests':guests,
        'location': location
    }
    return render(request, 'home.html', context)

