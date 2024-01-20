from django.contrib import admin
from django.urls import include ,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls')),
]

endpoint = 'http://127.0.0.1:8000/api'

