from django.contrib import admin
from django.urls    import path,include

urlpatterns = [

    path('vehicle/', include('vehicle_app.api.urls') ),
    path('permit/', include('permit_app.api.urls') ),
    path('admin/', admin.site.urls),

]


