from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User

from MyCRM.forms import PersonalInfoForm


class PersonalInfo(DetailView):
    model = User
    fields = '__all__'
    template_name = 'registration/myaccount.html'
    context_object_name = 'personal'
    pk_url_kwarg = 'user_id'
    extra_context = {'title': 'My account'}


def personal_info(request):
    form = PersonalInfoForm()
    form.initial['username'] = 'Antonn'
    form.initial['first_name'] = 'Anton'
    form.initial['email'] = 'anton.anton@gmail.com'
    if request.method == 'POST':
        print(request.POST)
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            print('form is valid')
            print(form.cleaned_data)
    context = {'form': form, 'title': 'My account'}
    return render(request, 'registration/myaccount.html', context=context)
