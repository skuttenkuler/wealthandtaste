from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from artists.models import Artist, GuestArtist


def index(request):
    artists = Artist.objects.all().order_by('order').values()
    guests = GuestArtist.objects.all()
    context = {
        'artists': artists,
        'guests':guests
    }
    return render(request, 'home.html', context)


