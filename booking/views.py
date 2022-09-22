from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from .forms import ClientForm
import environ
import os
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
from .forms import ClientForm

def index(request):
    return render(request,template_name='booking.html')

def new_client_form(request):
    if request.method == 'GET':
        form = ClientForm()
    else:
        form = ClientForm(request.POST)
        if form.is_valid():
            subject = 'New Client Tattoo Inquiry'
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            from_email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            location = form.cleaned_data['location']
            size = form.cleaned_data['size']
            description = form.cleaned_data['description']
            style = form.cleaned_data['style']
            reference = form.cleaned_data['reference']
            try:
                send_mail(
                        from_email, 
                        subject, 
                        first_name, 
                        last_name, 
                        phone, 
                        location, 
                        size, 
                        description, 
                        style, 
                        reference, 
                        ['admin@example.com']
                        )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            print('Email: success')
        form = {
            'form':form
        }
    return render(request,'booking.html',form)

