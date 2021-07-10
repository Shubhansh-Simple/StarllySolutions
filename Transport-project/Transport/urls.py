from django.contrib import admin
from django.urls    import path,include

urlpatterns = [
    path('', include('vehicle_app.api.urls') ),
    path('admin/', admin.site.urls),
]
