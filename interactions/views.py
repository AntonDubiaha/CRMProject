from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from clients.models import Client
from projects.models import Project
from .models import Interaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class InteractionsForClient(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Client
    template_name = 'interactions/interactions_client.html'
    pk_url_kwarg = 'client_id'
    extra_context = {'title': 'Interaction of client'}
    allow_empty = True
    permission_required = 'interactions.view_interaction'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['interactions_client_list'] = Interaction.objects.filter(client_id=self.kwargs['client_id']).order_by(
            self.request.GET.get('orderby', 'project'))
        return context


class InteractionsForProject(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Project
    template_name = 'interactions/interactions_project.html'
    pk_url_kwarg = 'project_id'
    extra_context = {'title': 'Interaction of project'}
    allow_empty = True
    permission_required = 'interactions.view_interaction'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['interactions_project_list'] = Interaction.objects.filter(
            project_id=self.kwargs['project_id']).order_by(self.request.GET.get('orderby', 'project'))
        return context


class InteractionsList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Interaction
    template_name = 'interactions/interactions_list.html'
    extra_context = {'title': 'All interactions'}
    permission_required = 'interactions.view_interaction'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['interactions_list'] = Interaction.objects.all().order_by(self.request.GET.get('orderby', 'project'))
        return context


class InteractionDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Interaction
    fields = '__all__'
    template_name = 'interactions/interaction_detail.html'
    pk_url_kwarg = 'interaction_id'
    context_object_name = 'interaction_detail'
    extra_context = {'title': 'Information of the interaction'}
    permission_required = 'interactions.view_interaction'


class InteractionCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Interaction
    fields = '__all__'
    template_name = 'interactions/interaction_create.html'
    success_url = reverse_lazy('interactions_list')
    extra_context = {'title': 'Create a interaction'}
    permission_required = 'interactions.add_interaction'


class InteractionUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Interaction
    fields = '__all__'
    template_name = 'interactions/interaction_update.html'
    pk_url_kwarg = 'interaction_id'
    success_url = reverse_lazy('interactions_list')
    extra_context = {'title': 'Edit the interaction'}
    permission_required = 'interactions.change_interaction'


class InteractionDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Interaction
    fields = '__all__'
    template_name = 'interactions/interaction_delete.html'
    pk_url_kwarg = 'interaction_id'
    success_url = reverse_lazy('interactions_list')
    extra_context = {'title': 'Delete the interaction'}
    permission_required = 'interactions.delete_interaction'
