from django.shortcuts import render
from django.views.generic import ListView
from .models import Client
# Create your views here.


class Home(ListView):
    model = Client
    template_name = 'home.html'
    context_object_name = 'client_info'
    extra_context = {'title': 'Home page'}


def about(request):
    return render(request, 'about.html')
