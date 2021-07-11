from rest_framework     import serializers
from vehicle_app.models import Practice, Vehicle

class PracticeSerializer( serializers.ModelSerializer ):

    class Meta:
        model  = Practice
        fields = '__all__'

class VehicleSerializer ( serializers.ModelSerializer ):

    class Meta:
        model  = Vehicle
        fields = '__all__'


