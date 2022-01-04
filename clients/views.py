from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Client
from clients.forms import ClientEditForm
# Create your views here.


class Home(ListView):
    model = Client
    paginate_by = 3
    template_name = 'clients/home.html'
    context_object_name = 'client_info'
    extra_context = {'title': 'Home page'}

    def get_ordering(self):
        return self.request.GET.get('orderby')


class ClientAbout(DetailView):
    model = Client
    template_name = 'clients/client_about.html'
    pk_url_kwarg = 'client_id'
    context_object_name = 'client_about'


class ClientEdit(UpdateView):
    model = Client
    fields = ['name_company', 'full_name_user', 'company_description', 'address']
    template_name = 'clients/client_edit.html'
    pk_url_kwarg = 'client_id'
    