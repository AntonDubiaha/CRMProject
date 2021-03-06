from django.urls import path
from .views import (InteractionsForClient, InteractionsForProject,
                    InteractionsList, InteractionDetail,
                    InteractionCreate, InteractionUpdate, InteractionDelete)

urlpatterns = [
    path('client/<int:client_id>/interactions/', InteractionsForClient.as_view(), name='interactions_client'),
    path('project/<int:project_id>/interactions/', InteractionsForProject.as_view(), name='interactions_project'),
    path('interactions/', InteractionsList.as_view(), name='interactions_list'),
    path('interactions/detail/<int:interaction_id>/', InteractionDetail.as_view(), name='interaction_detail'),
    path('interaction/create/', InteractionCreate.as_view(), name='interaction_create'),
    path('interaction/update/<int:interaction_id>/', InteractionUpdate.as_view(), name='interaction_update'),
    path('interaction/delete/<int:interaction_id>/', InteractionDelete.as_view(), name='interaction_delete'),
]