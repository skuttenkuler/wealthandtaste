from django import forms
from django.forms import ModelForm

class ClientForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email", max_length=100)
    description = forms.CharField(widget=forms.Textarea,label="Description", max_length=2000)
    reference = forms.ImageField()