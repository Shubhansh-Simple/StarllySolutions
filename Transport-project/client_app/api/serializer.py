from rest_framework    import serializers
from client_app.models import Client 


class ClientSerializer ( serializers.ModelSerializer ):
    fullname       = serializers.ReadOnlyField()
    client_details = serializers.HyperlinkedIdentityField( 
                                                view_name='client-detail-view',
                                                   )
    class Meta:
        model  = Client
        fields = ('fullname','client_details',)

class ClientDetailSerializer ( serializers.ModelSerializer ):

    class Meta:
        model  = Client
        fields = '__all__'


