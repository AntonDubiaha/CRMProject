from django.urls import path
from .views import Home, ClientAbout, ClientEdit
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('client/<int:client_id>/', ClientAbout.as_view(), name='client_about'),
    path('clientedit/', ClientEdit.as_view(), name = 'client_edit'),
]
