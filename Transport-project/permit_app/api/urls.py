from django.urls import path
from .views      import PermitListCreateView, PermitDetailUpdateDeleteView

urlpatterns = [

    path('',          PermitListCreateView ,        name='permit-list-create'),
    path('<str:pk>/', PermitDetailUpdateDeleteView, name='permit-detail-update-delete'),

]


