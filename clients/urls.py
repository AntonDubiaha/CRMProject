from django.urls import path
#from django.views.generic import TemplateView
from .views import Home

urlpatterns = [
    path('', Home.as_view(), name='home.html'),
    #path('about/', TemplateView.as_view(template_name="about.html")),
]
