from django.urls import path
from .views      import PermitListCreateView

urlpatterns = [

    path('', PermitListCreateView , name='permit-list-create'),

]


