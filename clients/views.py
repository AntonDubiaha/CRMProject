from .forms import ClientForm, ClientFormSet
from django.db import transaction
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Client
from django.urls import reverse_lazy
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
    template_name = 'clients/client_edit.html'
    form_class = ClientForm
    pk_url_kwarg = 'client_id'
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(ClientEdit, self).get_context_data(**kwargs)
        if self.request.POST:
            data['number'] = ClientFormSet(self.request.POST, instance=self.object)
        else:
            data['number'] = ClientFormSet(instance=self.object)
        return data

    def get_success_url(self):
        return reverse_lazy('clients:client_about', kwargs={'pk': self.object.pk})
