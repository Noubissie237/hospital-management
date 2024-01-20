from django.contrib.auth import views as auth_views
from django.urls import include ,path
from . import views
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'rdv', RendezVousListAPIView)


urlpatterns = [
    path('api/', include(router.urls)),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'registration/logged_outt.html'), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('patient/', views.HomeView.as_view(), name='liste-patient'),
    path('ajout_patient/', views.AjoutPatientList.as_view(), name='ajout_patient'),
    path('habitude/',views.AjoutPatient.as_view(), name='habitude'),
    path('create/', create_rdv, name='create'),
    path('home/', views.home , name ="home"),
    path('<str:room>/', views.room , name ="room"),
    path('checkview/', views.checkview , name ="checkview"),
    path('send/', views.send , name ="send"),
    path('getMessages/<str:room>/', views.getMessages , name ="getMessages"),

]