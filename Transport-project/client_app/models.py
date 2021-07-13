from django.db import models


class Client( models.Model ):
    first_name    = models.CharField( max_length=15 )
    last_name     = models.CharField( max_length=15 )
    email         = models.EmailField( unique=True )
    mobile_number = models.BigIntegerField( primary_key=True, 
                                            unique=True,
                                            blank=True  
                                          )
    registration_date = models.DateField( auto_now_add=True )

    class Meta:
        ordering = ['first_name','last_name']

    @property
    def fullname( self ):
        return self.first_name + ' ' + self.last_name

    def save( self, *args , **kwargs ):
        '''Title the first & last name before save'''

        self.first_name = self.first_name.lower().title()
        self.last_name  = self.last_name.lower().title()

        super( Client, self ).save( *args, **kwargs )

    def __str__(self):
        return self.fullname

    

