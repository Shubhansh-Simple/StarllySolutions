from rest_framework    import serializers
from client_app.models import Client 


###########
# client/ #
###########
class ClientSerializer ( serializers.ModelSerializer ):
    fullname       = serializers.ReadOnlyField()
    client_details = serializers.HyperlinkedIdentityField( 
                                                view_name='client-detail-view',
                                                read_only=True
                                                   )
    class Meta:
        model  = Client
        fields = ( 'fullname',
                   'client_details')

    '''
    def validate_mobile_number( self ):
        pass
        Just validate it's a 10 digit number or not.
    '''

####################
# client/<int:pk>/ #
####################
class ClientDetailSerializer ( serializers.ModelSerializer ):

    class Meta:
        model  = Client
        fields = '__all__'


