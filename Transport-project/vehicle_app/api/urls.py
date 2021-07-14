from django.urls import path
from .views      import VehicleListCreateView,\
                        VehiclePermitListView,\
                        VehicleDetailUpdateDeleteView, VehicleRegisteredPerMonth

urlpatterns = [

    path('',         VehicleListCreateView, name='vehicle-list-create'),
    path('permits/', VehiclePermitListView, name='vehicle-permit-list'),

    path('csv/',VehicleRegisteredPerMonth ),

    path('<str:pk>/',VehicleDetailUpdateDeleteView, name='vehicle-detail-update-delete'),


]


