from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Client
from tinymce import models as tinymce_models


class ClientEditForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
                'name_company',
                'full_name_user',
                'company_description',
                'address',
                ]

    widgets = {
        'name_company': forms.TextInput(attrs={'class': 'form-control'}),
        'full_name_user': forms.TextInput(attrs={'class': 'form-control'}),
        'company_description': forms.TextInput(attrs={'class': 'Description'}),
        'address': forms.TextInput(attrs={'class': 'form-control'}),
    }
