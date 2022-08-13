from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from artists.models import Artist
from location.models import Location


def index(request):
    artists = Artist.objects.all()
    location = Location.objects.all()
    context = {
        'artists': artists,
        'location': location
    }
    return render(request, 'home.html', context)

