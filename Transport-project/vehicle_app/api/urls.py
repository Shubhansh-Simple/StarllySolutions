from django.urls import path
from .views      import Practice_list_create_view,\
                        Practice_update_retrieve_delete_view,\
                        VehicleListCreateView

urlpatterns = [

    path('', VehicleListCreateView, name='vehicle-list-create'),

    path('<int:pk>/', Practice_update_retrieve_delete_view, 
                      name='practice-update'),
]


