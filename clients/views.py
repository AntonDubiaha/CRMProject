from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PhoneFormset, EmailFormset, CreateEmailFormset, CreatePhoneFormset
from django.views.generic import ListView, DetailView
from .models import Client
from django.urls.base import reverse_lazy
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class Home(LoginRequiredMixin, ListView):
    model = Client
    paginate_by = 3
    template_name = 'clients/home.html'
    context_object_name = 'client_info'
    extra_context = {'title': 'Home page'}

    def get_ordering(self):
        return self.request.GET.get('orderby')


class ClientAbout(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'clients/client_about.html'
    pk_url_kwarg = 'client_id'
    context_object_name = 'client_about'


class ClientCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    fields = '__all__'
    template_name = 'clients/client_create.html'
    success_url = reverse_lazy('home')
    permission_required = 'clients.add_client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create client'
        if self.request.POST:
            context['phone_formset'] = CreatePhoneFormset(self.request.POST, instance=self.object)
            context['phone_formset'].full_clean()

            context['email_formset'] = CreateEmailFormset(self.request.POST, instance=self.object)
            context['email_formset'].full_clean()
        else:
            context['phone_formset'] = CreatePhoneFormset(instance=self.object)
            context['email_formset'] = CreateEmailFormset(instance=self.object)
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


class ClientDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    fields = ['name_company', 'full_name_user', 'company_description', 'address']
    template_name = 'clients/client_delete.html'
    pk_url_kwarg = 'client_id'
    success_url = reverse_lazy('home')
    permission_required = 'clients.delete_client'


class ClientUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    fields = '__all__'
    template_name = 'clients/client_update.html'
    pk_url_kwarg = 'client_id'
    success_url = reverse_lazy('home')
    permission_required = 'clients.delete_client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit client'
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


def SignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            user_group = Group.objects.get(name='User')
            user_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'clients/signup.html', {'form': form})
