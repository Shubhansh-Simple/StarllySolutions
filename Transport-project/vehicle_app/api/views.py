from rest_framework            import status
from rest_framework.decorators import api_view
from rest_framework.response   import Response

from vehicle_app.models import Vehicle
from .serializer        import VehicleSerializer,\
                               VehicleSerializerWithPermits,\
                               VehicleDetailSerializer


@api_view( ['GET'] )
def VehiclePermitListView( request ):
    '''All vehicles with their permits'''

    if request.method == 'GET':
        vehicle_data   = Vehicle.objects.all()
        serialize_data = VehicleSerializerWithPermits( vehicle_data, many=True )
        return Response( serialize_data.data )


@api_view( ['GET','POST'] )
def VehicleListCreateView( request ):
    '''Vehicle create/ list/ endpoints'''

    if request.method == 'GET':

        vehicle_data   = Vehicle.objects.all()
        serialize_data = VehicleSerializer( vehicle_data, 
                                            many=True,
                                            context = {'request' : request} )

        return Response( serialize_data.data )

    elif request.method == 'POST':
        serialize_data = VehicleSerializer( data=request.data )

        if serialize_data.is_valid():
            serialize_data.save()
            return Response( serialize_data.data,
                             status=status.HTTP_201_CREATED )

        return Response( serialize_data.errors,
                         status=status.HTTP_400_BAD_REQUEST )


@api_view( ['GET','PUT','DELETE'] )
def VehicleDetailUpdateDeleteView( request,pk ):

    try:
        vehicle_data = Vehicle.objects.get( vehicle_number=pk)
    except Vehicle.DoesNotExist:
        return Response( { 
                            'error' : {
                              'code'    : 404,
                              'message' : 'Vehicle number does not exist.' 
                            }
                         },
                         status=status.HTTP_404_NOT_FOUND )

    if request.method == 'GET':
        serialize_data = VehicleDetailSerializer( vehicle_data )
        print('Serialize data -',serialize_data.data)
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





