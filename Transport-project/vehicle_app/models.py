from django.db         import models
from client_app.models import Client

class Vehicle( models.Model ):
    '''VEHICLE details and licensing'''

    CATEGORIES = ( 
                   ('DMG',  'DMG'),
                   ('Stockyard',  'Stock-Yard'),
                 )

    TYPE       = ( 
                   ('Tipper',  'Tipper'),
                   ('Tractor',  'Tractor'),
                   ('Lorry',  'Lorry'),
                 )

    INSTALLATION_TYPE = (
                          ( 'New Installation', 'New Installation' ),
                          ( 'Migration', 'Migration' ),
                          ( 'Renewal with existing hardware', 
                            'Renewal with existing hardware'  ),
                        )

    vehicle_owner     = models.ForeignKey( Client, on_delete=models.PROTECT )
    vehicle_number    = models.CharField( max_length=20 )
    gps_imei          = models.BigIntegerField( default=0 )
    license_start     = models.DateField()
    license_end       = models.DateField()
    vehicle_category  = models.CharField( choices=CATEGORIES, 
                                          max_length=9,
                                          default=CATEGORIES[0][0]
                                        )
    vehicle_type      = models.CharField( choices=TYPE, 
                                          max_length=15,
                                          default=TYPE[0][0]
                                        )
    total_permits     = models.PositiveIntegerField( default=0 )

    installation_type = models.CharField( choices=INSTALLATION_TYPE, 
                                          max_length=30,
                                          default=INSTALLATION_TYPE[0][0]
                                        )
    registration_date = models.DateField()

    @property
    def license_status(self):
        '''Weather the today's date is b/w the start and end date.'''
        return True

    @property
    def increase_permits(self):
        self.total_permits += 1


class Practice( models.Model ):
    first_name = models.CharField( max_length=10 )
    last_name  = models.CharField( max_length=10 )

    def __str__(self):
        return f'{self.first_name.title()} {self.last_name}'

