from rest_framework     import  serializers
from permit_app.models  import  Permit

from vehicle_app.models import Vehicle


class VehiclePermitSerializer( serializers.ModelSerializer ):
    '''Vehicle serializer specially for permit data representation'''

    vehicle_owner = serializers.StringRelatedField()

    class Meta:
        model  = Vehicle 
        fields = ( 'vehicle_number',
                   'vehicle_owner',
                   'gps_imei',
                   'vehicle_category',
                   'vehicle_type')


class PermitSerializer ( serializers.ModelSerializer ):

    # we will come back here
    vehicle = VehiclePermitSerializer( read_only=True )

    class Meta:
        model  = Permit
        fields = '__all__'





