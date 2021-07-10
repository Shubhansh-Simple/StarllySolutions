from django.contrib            import admin
from django.contrib.auth.admin import UserAdmin

from .forms  import ClientChangeForm , ClientCreationForm
from .models import Client

class ClientAdmin( UserAdmin ):
    add_form  = ClientCreationForm
    form      = ClientChangeForm
    model     = Client

admin.site.register( Client,ClientAdmin )


