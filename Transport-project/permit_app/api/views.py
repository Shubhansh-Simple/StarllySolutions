from rest_framework            import status
from rest_framework.decorators import api_view
from rest_framework.response   import Response

from permit_app.models  import  Permit
from .serializer        import PermitSerializer

@api_view( ['GET','POST'] )
def PermitListCreateView( request ):
    '''Permit create/ list/ endpoints'''

    if request.method == 'GET':

        permit_data    = Permit.objects.all()
        serialize_data = PermitSerializer( permit_data, many=True )

        return Response( serialize_data.data )




