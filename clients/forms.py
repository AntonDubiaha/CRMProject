from .models import Client, Phone, Email
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


PhoneFormset = inlineformset_factory(Client, Phone, fields=('number',), can_delete=True, extra=1)
EmailFormset = inlineformset_factory(Client, Email, fields=('email',), can_delete=True, extra=1)
CreatePhoneFormset = inlineformset_factory(Client, Phone, fields=('number',), can_delete=True, extra=4)
CreateEmailFormset = inlineformset_factory(Client, Email, fields=('email',), can_delete=True, extra=4)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
