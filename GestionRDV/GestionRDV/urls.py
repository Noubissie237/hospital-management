from django.contrib import admin
from django.urls import include ,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('App.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

endpoint = 'http://127.0.0.1:8000/api'

