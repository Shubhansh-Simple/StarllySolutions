from django.db          import models
from vehicle_app.models import Vehicle

class Permit( models.Model ):
    '''Vehicle's PERMIT to transport goods'''

    vehicle         = models.ForeignKey( Vehicle, on_delete=models.DO_NOTHING )

    permit_number   = models.CharField( max_length=20 )
    loading_point   = models.CharField( max_length=20 )
    unloading_point = models.CharField( max_length=20 )
    quanity         = models.FloatField()

    def __str__( self ):
        return str( self.vehicle ) + ' ' +str( self.loading_point )


