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
def detail(request, artists):
    return HttpResponse("<h2>Artist: " + artists.first_name + " " + artists.last_name +"</h2>")