from rest_framework     import serializers
from vehicle_app.models import Vehicle
from permit_app.models  import Permit

class PermitVehicleSerializer( serializers.ModelSerializer ):
    '''Permit serializer specially for vehicle data representation'''

    class Meta:
        model  = Permit
        fields = ('permit_date','permit_number',)
        depth = 1


class VehicleSerializer ( serializers.ModelSerializer ):
    license_status   = serializers.ReadOnlyField()

    # for post request
    vehicle_owner_id = serializers.IntegerField()
    vehicle_owner = serializers.HyperlinkedRelatedField( 
                                                read_only=True,
                                                view_name='client-detail-view',
                                                   )

    class Meta:
        model  = Vehicle
        fields = '__all__'
        read_only_fields = ( 'license_end',
                             'total_permits',
                             'vehicle_owner',
                             'license_status' )
        extra_kwargs = {
            'vehicle_owner_id' : { 'write_only' : True },
        }


class VehicleSerializerWithPermits( serializers.ModelSerializer ):
    vehicle_owner = serializers.StringRelatedField()
    vechicle_permits = PermitVehicleSerializer( many=True )

    class Meta:
        model  = Vehicle
        fields = '__all__'




