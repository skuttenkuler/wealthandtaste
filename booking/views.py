from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ClientForm

def index(request):
    form = ClientForm(request.POST or None)
    context = {
        'form':form
    }
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            subject = 'New Client Inquiry'
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            location = form.cleaned_data['location']
            size = form.cleaned_data['size']
            description = form.cleaned_data['description']
            style = form.cleaned_data['style']
            print(description)
            html = render_to_string('newClientForm.html', context)
            # print(context)
            try:
                send_mail(  subject,
                            html_message=html,
                            from_email=settings.DEFAULT_FROM_EMAIL,
                            recipient_list=[''],
                            fail_silently=False
                )
            except BadHeaderError:
                return HttpResponse("invalid header")
            return redirect("booking")

    return render(request,'booking.html',{'form':form})




