from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PhoneFormset, EmailFormset
from django.views.generic import ListView, DetailView
from .models import Client, Phone, Email
from django.urls.base import reverse_lazy


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
    fields = '__all__'
    template_name = 'clients/client_edit.html'
    pk_url_kwarg = 'client_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit company'
        if self.request.POST:
            context['phone_formset'] = PhoneFormset(self.request.POST, instance=self.object)
            context['phone_formset'].full_clean()

            context['email_formset'] = EmailFormset(self.request.POST, instance=self.object)
            context['email_formset'].full_clean()
        else:
            context['phone_formset'] = PhoneFormset(instance=self.object)
            context['email_formset'] = EmailFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        phone_formset = context['phone_formset']
        email_formset = context['email_formset']
        if phone_formset.is_valid() and email_formset.is_valid():
            response = super().form_valid(form)
            phone_formset.instance = self.object
            phone_formset.save()
            email_formset.instance = self.object
            email_formset.save()
            return response
        else:
            return super().form_invalid(form)


class ClientCreate(CreateView):
    model = Client
    fields = '__all__'
    template_name = 'clients/client_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create company'
        if self.request.POST:
            context['phone_formset'] = PhoneFormset(self.request.POST, instance=self.object)
            context['phone_formset'].full_clean()

            context['email_formset'] = EmailFormset(self.request.POST, instance=self.object)
            context['email_formset'].full_clean()
        else:
            context['phone_formset'] = PhoneFormset(instance=self.object)
            context['email_formset'] = EmailFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        phone_formset = context['phone_formset']
        email_formset = context['email_formset']
        if phone_formset.is_valid() and email_formset.is_valid():
            response = super().form_valid(form)
            phone_formset.instance = self.object
            phone_formset.save()
            email_formset.instance = self.object
            email_formset.save()
            return response
        else:
            return super().form_invalid(form)


class ClientDelete(DeleteView):
    model = Client
    fields = ['name_company', 'full_name_user', 'company_description', 'address']
    template_name = 'clients/client_edit.html'
    pk_url_kwarg = 'client_id'


class PhoneUpdate(UpdateView):
    model = Phone
    fields = ['number']
    template_name = 'clients/client_edit.html'
    pk_url_kwarg = 'client_id'


class EmailUpdate(UpdateView):
    model = Email
    fields = ['email']
    template_name = 'clients/client_edit.html'
    pk_url_kwarg = 'client_id'
