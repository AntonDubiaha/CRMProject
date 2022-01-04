from django.contrib import admin
from .models import Client, Phone, Email

# Register your models here.


class PhoneInLine(admin.TabularInline):
    model = Phone
    extra = 0


class EmailInline(admin.TabularInline):
    model = Email
    extra = 0


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name_company', 
                    'full_name_user', 
                    'created', 
                    'updated', 
                    'address', 
                    'company_description')
    inlines = [PhoneInLine, EmailInline]


admin.site.register(Client, ClientAdmin)
admin.site.register(Phone)
admin.site.register(Email)
