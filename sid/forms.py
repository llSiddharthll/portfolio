# contact/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name', 'required': 'true'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'required': 'true'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Subject', 'required': 'true'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message..', 'required': 'true', 'cols': '30', 'rows': '10'}))
