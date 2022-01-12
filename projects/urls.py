from django.urls import path
from .views import ProjectList, ProjectCreate, ProjectDelete, ProjectDetail, ProjectUpdate, ClientProjectList

urlpatterns = [
    path('list/', ProjectList.as_view(), name='project_list'),
    path('detail/<int:project_id>/', ProjectDetail.as_view(), name='project_detail'),
    path('create/', ProjectCreate.as_view(), name='create_project'),
    path('update/<int:project_id>/', ProjectUpdate.as_view(), name='update_project'),
    path('delete/<int:project_id>/', ProjectDelete.as_view(), name='delete_project'),
]

project_client_list_patterns = [
    path('client/<int:client_id>/projects/list/', ClientProjectList.as_view(), name='client_project_list'),
]
