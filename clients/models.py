from django.db import models

# Create your models here.


class Client(models.Model):
    name_company = models.CharField(max_length=200)
    full_name_user = models.CharField(max_length=100)
    company_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name_user


class MobileNumber(models.Model):
    number = models.CharField(max_length=20, help_text='Enter phone number.')
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class Email(models.Model):
    email = models.EmailField(help_text='Enter e-mail address.')
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.email
