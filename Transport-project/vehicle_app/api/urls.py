from django.urls import path
from .views      import VehicleListCreateView,\
                        VehiclePermitListView,\
                        VehicleDetailUpdateDeleteView

urlpatterns = [

    path('',         VehicleListCreateView, name='vehicle-list-create'),
    path('permits/', VehiclePermitListView, name='vehicle-permit-list'),
]


