from rest_framework            import status
from rest_framework.decorators import api_view
from rest_framework.response   import Response

from permit_app.models  import Permit
from .serializer        import PermitSerializer

############
# /permit/ #
############
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

        print( 'At least see - ',serialize_data.data )
        return Response( serialize_data.errors,
                         status=status.HTTP_400_BAD_REQUEST )


#####################
# /permit/<str:pk>/ #
#####################
@api_view( ['GET','PUT', 'DELETE'] )
def PermitDetailUpdateDeleteView( request,pk ):

    try:
        permit_data = Permit.objects.get( permit_number=pk )
    except Permit.DoesNotExist:
        return Response( { 
                            'error' : {
                              'code'    : 404,
                              'message' : 'Permit number does not exist.' 
                            }
                         },
                         status=status.HTTP_404_NOT_FOUND )

    # DETAIL
    if request.method == 'GET':
        serialize_data = PermitSerializer( permit_data )
        return Response( serialize_data.data )

    # UPDATE 
    elif request.method == 'PUT':
        serialize_data = PermitSerializer( permit_data, data=request.data )

        if serialize_data.is_valid():
            serialize_data.save()
            return Response( serialize_data.data )

        return Response( serialize_data.errors,
                         status=status.HTTP_400_BAD_REQUEST )

    # DELETE
    elif request.method == 'DELETE':
        permit_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








