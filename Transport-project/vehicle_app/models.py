from django.db              import models
from client_app.models      import Client
from dateutil.relativedelta import relativedelta
from datetime               import date 


class Vehicle( models.Model ):
    '''VEHICLE details and licensing'''

    CATEGORIES = ( 
                   ('DMG',  'DMG'),
                   ('Stockyard',  'Stockyard'),
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

    vehicle_number    = models.CharField( max_length=20,primary_key=True )
    gps_imei          = models.BigIntegerField( unique=True )
    license_start     = models.DateField()
    license_end       = models.DateField( blank=True )

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
                                          default=INSTALLATION_TYPE[0][0] )

    registration_date = models.DateField()
    vehicle_owner     = models.ForeignKey( Client, 
                                           on_delete=models.PROTECT )

    class Meta:
        ordering = ['-vehicle_number','-registration_date']

    # before making any permits
    @property
    def license_status(self):
        '''Is today's date is b/w the start and end license date.'''

        return self.license_start <= date.today() <= self.license_end

    @property
    def increase_permits(self):
        self.total_permits += 1

    def save( self, *args , **kwargs ):
        '''Auto filled license end date'''

        if self._state.adding: # or self.license_start changed
            self.license_end = self.license_start + relativedelta(years=1)

        self.vehicle_number = self.vehicle_number.lower()

        super( Vehicle,self ).save( *args , **kwargs )

    def __str__(self):
        return f'{self.vehicle_number} - {self.vehicle_owner}'


