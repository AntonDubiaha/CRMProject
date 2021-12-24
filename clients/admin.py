from django.contrib import admin
from .models import Client, MobileNumber, Email

# Register your models here.

admin.site.register(Client)
admin.site.register(MobileNumber)
admin.site.register(Email)


class MobileNumberInLine(admin.TabularInline):
    model = MobileNumber
    extra = 0


class ClientAdmin(admin.ModelAdmin):
    model = Client
    inlines = [MobileNumberInLine]
