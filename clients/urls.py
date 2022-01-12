from django.urls import path
from .views import Home, ClientAbout, ClientCreate, ClientUpdate, ClientDelete

urlpatterns = [
    path('client/<int:client_id>/', ClientAbout.as_view(), name='client_about'),
    path('create/', ClientCreate.as_view(), name='client_create'),
    path('update/<int:client_id>/', ClientUpdate.as_view(), name='client_update'),
    path('delete/<int:client_id>/', ClientDelete.as_view(), name='client_delete'),
]

home_patterns = [
    path('', Home.as_view(), name='home'),
]
