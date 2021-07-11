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
    vehicle_owner = serializers.StringRelatedField()

    class Meta:
        model  = Vehicle
        fields = '__all__'

class VehicleSerializerWithPermits( serializers.ModelSerializer ):
    vehicle_owner = serializers.StringRelatedField()
    vechicle_permits = PermitVehicleSerializer( many=True )

    class Meta:
        model  = Vehicle
        fields = '__all__'




