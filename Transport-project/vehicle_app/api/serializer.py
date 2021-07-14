from rest_framework     import serializers
from vehicle_app.models import Vehicle
from permit_app.models  import Permit

# for vehicle detail page
from client_app.api.serializer import ClientDetailSerializer

#############
# /vehicle/ #
#############
class VehicleSerializer ( serializers.ModelSerializer ):
    license_status   = serializers.ReadOnlyField()

    # for post request
    vehicle_owner_id = serializers.IntegerField( write_only=True )
    vehicle_owner = serializers.HyperlinkedRelatedField( 
                                                read_only=True,
                                                view_name='client-detail-view',
                                                   )

    class Meta:
        model  = Vehicle
        fields = '__all__'
        read_only_fields = ( 'license_end',
                             'total_permits' )


######################
# /vehicle/<int:pk>/ #
######################
class VehicleDetailSerializer ( serializers.ModelSerializer ):
    license_status   = serializers.BooleanField( read_only=True )
    vehicle_owner    = ClientDetailSerializer( read_only=True )

    # for post request
    vehicle_owner_id = serializers.IntegerField( write_only=True )

    class Meta:
        model  = Vehicle
        fields = '__all__'
        read_only_fields = ( 'license_end',
                             'total_permits',
                             'license_status' )

#####################
# /vehicle/permits/ #
#####################
class PermitVehicleSerializer( serializers.ModelSerializer ):
    '''Permit serializer specially for vehicle data representation'''

    class Meta:
        model  = Permit
        fields = ('permit_date','permit_number',)

class VehicleSerializerWithPermits( serializers.ModelSerializer ):
    '''All Vehicles with total permits number and dates list'''

    vehicle_owner = serializers.StringRelatedField()
    vechicle_permits = PermitVehicleSerializer( many=True )

    class Meta:
        model  = Vehicle
        fields = '__all__'


