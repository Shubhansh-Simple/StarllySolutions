from rest_framework            import status
from rest_framework.decorators import api_view
from rest_framework.response   import Response

from vehicle_app.models import Vehicle
from client_app.models  import Client
from .serializer        import VehicleSerializer,\
                               VehicleSerializerWithPermits,\
                               VehicleDetailSerializer

#####################
# /vehicle/permits/ #
#####################
@api_view( ['GET'] )
def VehiclePermitListView( request ):
    '''All vehicles with their permits'''

    if request.method == 'GET':
        vehicle_data   = Vehicle.objects.all()
        serialize_data = VehicleSerializerWithPermits( vehicle_data, many=True )
        return Response( serialize_data.data )


#############
# /vehicle/ #
#############
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
        serialize_data = VehicleDetailSerializer( data=request.data )

        if serialize_data.is_valid():
            #Check owner exist or not

            vehicle_owner_id = serialize_data.validated_data.get('vehicle_owner_id')

            try:
                Client.objects.get(mobile_number=vehicle_owner_id)
            except Client.DoesNotExist:
                return Response( { 
                            'error' : {
                              'code'    : 400,
                              'message' : 'Client does not exist.' 
                            }
                         },
                         status=status.HTTP_400_BAD_REQUEST )

            serialize_data.save()

            return Response( serialize_data.data,
                             status=status.HTTP_201_CREATED )

        return Response( serialize_data.errors,
                         status=status.HTTP_400_BAD_REQUEST )


######################
# /vehicle/<int:pk>/ #
######################
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

    # DETAIL
    if request.method == 'GET':
        serialize_data = VehicleDetailSerializer( vehicle_data )
        return Response( serialize_data.data )

    # UPDATE 
    elif request.method == 'PUT':
        serialize_data = VehicleDetailSerializer( vehicle_data, data=request.data )

        if serialize_data.is_valid():
            serialize_data.save()
            return Response( serialize_data.data )

        return Response( serialize_data.errors,
                         status=status.HTTP_400_BAD_REQUEST )

    # DELETE
    elif request.method == 'DELETE':
        vehicle_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





