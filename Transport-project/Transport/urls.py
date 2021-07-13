from django.contrib import admin
from django.urls    import path,include

urlpatterns = [

    # login
    path('api-auth/',      include('rest_framework.urls') ), # for browersable api
    path('api/rest-auth/', include('rest_auth.urls') ),

    path('vehicle/', include('vehicle_app.api.urls') ),
    path('permit/',  include('permit_app.api.urls') ),
    path('client/',  include('client_app.api.urls') ),
    path('admin/', admin.site.urls),

]


