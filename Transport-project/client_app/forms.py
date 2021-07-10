from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django  import forms

from .models import Client

class ClientCreationForm( UserCreationForm ):

    class Meta( UserCreationForm.Meta ):
        model  = Client
        fields = UserCreationForm.Meta.fields


class ClientChangeForm( UserChangeForm ):

    class Meta:
        model  = Client
        fields = UserChangeForm.Meta.fields


class ClientCreateForm( forms.ModelForm ):
    class Meta:
        model   = Client
        fields  = (
                    'first_name','last_name','email','phone_number',
                  )


