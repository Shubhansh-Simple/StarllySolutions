from django.db          import models
from vehicle_app.models import Vehicle

class Permit( models.Model ):
    '''Vehicle's PERMIT to transport goods'''

    vehicle         = models.ForeignKey( Vehicle, on_delete=models.DO_NOTHING )

    permit_number   = models.CharField( max_length=20, unique=True )
    loading_point   = models.CharField( max_length=20 )
    unloading_point = models.CharField( max_length=20 )
    quanity         = models.FloatField()
    #permit_date    = models.DateField()

    def save( self, *args , **kwargs ):
        '''Call methods before save'''

        self.loading_point   = self.loading_point.lower().title()
        self.unloading_point = self.unloading_point.lower().title()

        if self._state.adding:
            # if new instance created

            self.vehicle.increase_permits
            self.vehicle.save()

        super( Permit,self ).save( *args , **kwargs )


    def __str__( self ):
        return str( self.vehicle ) + ' ' +str( self.loading_point )


