from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail,EmailMessage,BadHeaderError
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from .forms import ClientForm

def index(request):
    form = ClientForm(request.POST,request.FILES)
    context = {
        'form':form
    }
    if request.method == 'POST':
        if form.is_valid():
            #print(form.cleaned_data)
            subject = 'New Client Inquiry'
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            desc = form.cleaned_data['description']
            form_data = {
                'name':name,
                'email':email,
                'desc':desc
            }
            html_message = render_to_string('newClientForm.html',{'data':form_data})
            plain_message = strip_tags(html_message)
            # print("Email:", settings.EMAIL)
            try:
                #print(subject,html)
                email = EmailMessage(   subject,
                                        plain_message,
                                        settings.FROM_EMAIL,
                                        [settings.TO_EMAIL]
                )
                if request.FILES:
                    uploaded_file = request.FILES['reference'] # file is the name value which you have provided in form for file field
                    email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
                    email.send()     
            except BadHeaderError:
                return HttpResponse("invalid header")
            return redirect("booking")
    return render(request,'booking.html',{'form':form})




