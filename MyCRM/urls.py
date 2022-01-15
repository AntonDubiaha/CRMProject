from django.contrib import admin
from django.urls import path, include
from clients.urls import home_patterns, signup_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_patterns)),
    path('client/', include('clients.urls')),
    path('project/', include('projects.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(signup_patterns)),
    path('', include('interactions.urls')),
]
