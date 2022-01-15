from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from projects.models import Project
from clients.models import Client
from django.urls.base import reverse_lazy


class ProjectList(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'project_list'
    extra_context = {'title': 'All projects'}


class ClientProjectList(DetailView):
    model = Client
    template_name = 'projects/client_project_list.html'
    pk_url_kwarg = 'client_id'
    extra_context = {'title': 'Projects of company:'}
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_project_list'] = Project.objects.filter(client_id=self.kwargs['client_id'])
        return context


class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    pk_url_kwarg = 'project_id'
    context_object_name = 'detail_project'
    extra_context = {'title': 'Information of the project'}


class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'
    template_name = 'projects/create_project.html'
    pk_url_kwarg = 'project_id'
    extra_context = {'title': 'Create project'}
    success_url = reverse_lazy('project_list')


class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'projects/update_project.html'
    pk_url_kwarg = 'project_id'
    extra_context = {'title': 'Edit project'}
    success_url = reverse_lazy('project_list')


class ProjectDelete(DeleteView):
    model = Project
    fields = '__all__'
    template_name = 'projects/delete_project.html'
    pk_url_kwarg = 'project_id'
    extra_context = {'title': 'Delete project'}
    success_url = reverse_lazy('project_list')
