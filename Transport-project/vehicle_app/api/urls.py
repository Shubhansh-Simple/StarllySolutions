from django.urls import path
from .views      import VehicleListCreateView,VehiclePermitListView

urlpatterns = [

    path('',         VehicleListCreateView, name='vehicle-list-create'),
    path('permits/', VehiclePermitListView, name='vehicle-permit-list'),
]


