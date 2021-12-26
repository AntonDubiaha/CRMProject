from django.shortcuts import render
from django.views.generic import ListView
from .models import Client
# Create your views here.


class Home(ListView):
    model = Client
    template_name = 'clients/home.html'
    context_object_name = 'client_info'
    extra_context = {'title': 'Home page'}

    def get_ordering(self):
      return self.request.GET.get('orderby')


def about(request):
    return render(request, 'about.html')
