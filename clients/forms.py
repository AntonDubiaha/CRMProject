from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Client

class ClientEditForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = '__all__'
