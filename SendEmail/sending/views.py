from django.core import mail
from SendEmail.settings import EMAIL_HOST_USER
from django.shortcuts import render
from .forms import *


def index(request):
    text = ""
    if request.method == "POST":
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            text = "Sent"
            to_mail = request.POST.get('email')
            message = request.POST.get('message')
            file = request.FILES['file']
            m_mail = mail.EmailMessage(
                '',
                message,
                EMAIL_HOST_USER,
                [to_mail],
            )
            m_mail.attach(file.name, file.read(), file.content_type)
            m_mail.send(fail_silently=False)

    form = EmailForm
    context = {
        'form': form,
        'message': text,
    }
    return render(request, 'sending/index.html', context)
