from django.contrib import admin
from django.urls import path, include
from projects.urls import project_client_list_patterns
from clients.urls import home_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_patterns)),
    path('client/', include('clients.urls')),
    path('project/', include('projects.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', include(project_client_list_patterns)),
]
