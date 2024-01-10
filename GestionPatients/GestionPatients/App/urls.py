from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, home

router = DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', home, name='Accueil'),
    path('api/', include(router.urls)),
]
