from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Client


class ClientEditForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name_company', 'full_name_user']

    widgets = {
        'name_company': forms.TextInput(attrs={'class': 'form-control'}),
        'full_name_user': forms.TextInput(attrs={'class': 'form-control'}),
    }
