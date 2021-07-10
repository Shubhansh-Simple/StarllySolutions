from rest_framework     import serializers
from vehicle_app.models import Practice

class PracticeSerializer( serializers.ModelSerializer ):

    class Meta:
        model  = Practice
        fields = '__all__'



