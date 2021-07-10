'''
	CUSTOMER USER MODEL
'''

from django.contrib.auth.models import AbstractUser
from django.db                  import models


class Client( AbstractUser ):
    phone_number = models.BigIntegerField()
    

