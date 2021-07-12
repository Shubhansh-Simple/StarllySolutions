from rest_framework            import status
from rest_framework.decorators import api_view
from rest_framework.response   import Response

from permit_app.models  import Permit
from .serializer        import PermitSerializer

@api_view( ['GET','POST'] )
def PermitListCreateView( request ):
    '''Permit create/ list/ endpoints'''

    if request.method == 'GET':

        permit_data    = Permit.objects.all()
        serialize_data = PermitSerializer( permit_data, many=True )

        return Response( serialize_data.data )

    elif request.method == 'POST':

        serialize_data = PermitSerializer( data=request.data )
        if serialize_data.is_valid():
            serialize_data.save()
            return Response( serialize_data.data,
                             status=status.HTTP_201_CREATED )

        return Response( serialize_data.errors,
                         status=status.HTTP_400_BAD_REQUEST )



