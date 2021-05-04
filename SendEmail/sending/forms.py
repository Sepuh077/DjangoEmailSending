from django.forms import ModelForm
from django import forms
from .models import *


class EmailForm(ModelForm):
    class Meta:
        model = SendEmailModel
        fields = ['email', 'message', 'file']

        widgets = {
            'email': forms.TextInput(attrs={'size': 10}),
            'message': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
        }
