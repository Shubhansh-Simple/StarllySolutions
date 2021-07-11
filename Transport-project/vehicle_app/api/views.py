from rest_framework            import status
from rest_framework.decorators import api_view
from rest_framework.response   import Response

from vehicle_app.models import Vehicle
from .serializer        import VehicleSerializer, VehicleSerializerWithPermits


@api_view( ['GET','POST'] )
def VehicleListCreateView( request ):
    '''Vehicle create/ list/ endpoints'''

    if request.method == 'GET':

        vehicle_data   = Vehicle.objects.all()
        serialize_data = VehicleSerializer( vehicle_data, many=True )

        return Response( serialize_data.data )


@api_view( ['GET'] )
def VehiclePermitListView( request ):

    if request.method == 'GET':
        vehicle_data   = Vehicle.objects.all()
        serialize_data = VehicleSerializerWithPermits( vehicle_data, many=True )
        return Response( serialize_data.data )















































@api_view( ['GET', 'PUT', 'DELETE'] )
def Practice_update_retrieve_delete_view( request, pk ):

    try:
        practice = Practice.objects.get(id=pk)
    except Practice.DoesNotExist:
        return Response({'error' : {
                'code' : 404,
                'message' : 'Practice id not found',
            }},  status=status.HTTP_404_NOT_FOUND )

    if request.method == 'GET':
        serializer = PracticeSerializer( practice )

        return Response( serializer.data )

    elif request.method == 'DELETE':
        practice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = PracticeSerializer( practice , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data )
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )





