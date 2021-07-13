'''
    For adding user detail with the 
    Token after login.
'''
from rest_framework import serializers 
from django.contrib.auth import get_user_model
from rest_auth.models import TokenModel

class UserSerializer( serializers.ModelSerializer ):
    class Meta:
        model = get_user_model()
        #fields = '__all__'
        fields = ( 'id',
                   'last_login',
                   'username',
                   'email',
                   'password',
                   'first_name',
                   'last_name', )
        extra_kwargs = {
            'password' : { 'write_only' : True }
        }

class TokenSerializer(serializers.ModelSerializer):
    '''Customer Serializer for Token model'''

    user = UserSerializer(many=False, read_only=True)  # this is add by myself.
    class Meta:
        model = TokenModel
        fields = ('key', 'user')
