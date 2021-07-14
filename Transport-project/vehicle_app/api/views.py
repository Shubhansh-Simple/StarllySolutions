from rest_framework            import status
from rest_framework.decorators import api_view
from rest_framework.response   import Response

# model
from vehicle_app.models import Vehicle
from client_app.models  import Client

# serializer
from .serializer        import VehicleSerializer,\
                               VehicleSerializerWithPermits,\
                               VehicleDetailSerializer
# FOR CSV
import csv
from django.http               import HttpResponse
from django.db.models          import Count


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



#################
# /vehicle/csv/ #
#################

@api_view( ['GET'] )
def VehicleRegisteredPerMonth(request):
    if request.method == 'GET':
        
        response = HttpResponse( content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="first.csv"'

        vehicle_data   = Vehicle.objects.values(
                                'registration_date__month',
                                'installation_type'
                            ).annotate(
                                    total_registration=Count('vehicle_number')
                                ).order_by('registration_date__month')

        header = [ 'total_registration',
                   'registration_date__month',
                   'installation_type' ]

        writer = csv.DictWriter(response, fieldnames=header)
        writer.writeheader()

        for x in vehicle_data:
            writer.writerow(x)

        return response




