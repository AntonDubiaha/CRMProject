from django import forms


class PersonalInfoForm(forms.Form):
    username = forms.CharField(max_length=50,)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()
