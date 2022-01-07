from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models
from django.urls import reverse

# Create your models here.


class Client(models.Model):
    '''создал модель клиента и описал её параметры'''
    name_company = models.CharField(max_length=200)
    full_name_user = models.CharField(max_length=100)
    company_description = tinymce_models.HTMLField('Description')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name_company

    def get_absolute_url(self):
        return reverse('client_about', kwargs={'client_id': self.pk}) 
    

class Phone(models.Model):
    '''создал модель телефонов и описал её параметры'''
    number = models.CharField(max_length=20, help_text='Enter phone number.')
    client = models.ForeignKey('Client', related_name="client_phones", on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class Email(models.Model):
    '''создал модель почт и описал её параметры'''
    email = models.EmailField(help_text='Enter e-mail address.')
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.email
