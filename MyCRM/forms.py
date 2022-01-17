from django import forms


class PersonalInfoForm(forms.Form):
    username = forms.CharField(max_length=50,)
