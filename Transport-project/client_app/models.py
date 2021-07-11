'''
	CUSTOMER USER MODEL
'''

from django.contrib.auth.models import AbstractUser
from django.db                  import models


class Client( AbstractUser ):
    phone_number = models.BigIntegerField( primary_key=True, 
                                           blank=True,
                                           unique=True,
                                           default=0 )

    def __str__(self):
        return self.username

    

