from django.urls import path
from .views      import ClientListCreateView

urlpatterns = [

    path('', ClientListCreateView , name='user-list-create'),

]
