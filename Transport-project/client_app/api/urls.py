from django.urls import path
from .views      import ClientListCreateView, ClientDetailView 

urlpatterns = [

    path('',          ClientListCreateView, name='client-list-create'),
    path('<int:pk>/', ClientDetailView,     name='client-detail-view'),

]
