from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                f'{subject} - {name}',
                message,
                email,
                ['llsiddharthtiwarill@gmail.com']  # your email address
            )

            # Redirect after successful submission
            return HttpResponseRedirect('/success/')
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})

def success(request):
    return render(request,'success.html')
    
