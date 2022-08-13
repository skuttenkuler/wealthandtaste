from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from artists.models import Artist


def index(request):
    artists = Artist.objects.all()
    context = {
        'artists': artists
    }
    return render(request, 'home.html', context)

