from django import forms
from django.forms import ModelForm

class ClientForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="First Name", max_length=100)
    email = forms.EmailField(label="Email", max_length=100)
    phone = forms.CharField(label="Phone", max_length=10)
    location = forms.CharField(label="Location of tattoo", max_length=100)
    size = forms.CharField(label="Rough size of tattoo", max_length=100)
    description = forms.CharField(label="Rough size of tattoo", max_length=100)
    style = forms.CharField(label="Style? Color? Black and Grey?", max_length=100)
    reference = forms.ImageField()