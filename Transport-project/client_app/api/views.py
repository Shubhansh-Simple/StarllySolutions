from rest_framework            import status
from rest_framework.decorators import api_view
from rest_framework.response   import Response

from client_app.models import Client
from .serializer       import ClientSerializer

@api_view( ['GET','POST'] )
def ClientListCreateView( request ):

    if request.method == 'GET':

        client_data    = Client.objects.all()
        serialize_data = ClientSerializer( client_data, many=True )

        return Response( serialize_data.data )

    elif request.method == 'POST':

        serializer = ClientSerializer( data=request.data )

        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, 
                             status=status.HTTP_201_CREATED )
        else:
            return Response( serializer.errors, 
                             status=status.HTTP_400_BAD_REQUEST )




