from django.shortcuts import render
from django.conf import settings
from core.settings import EMAIL_HOST_USER
from . import forms
from .forms import EmailForm
from django.core.mail import send_mail

def email(request):
    sub=forms.EmailForm()
    if request.method=='POST':
        sub=forms.EmailForm(request.POST)
        subject = 'Welcome to Presets'
        message = 'Hope you are enjoying'
        recepient = str(sub['Email'].value())
        send_mail(subject ,message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'subscribe.html', {'form':sub})

