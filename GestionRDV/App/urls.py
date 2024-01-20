from django.contrib.auth import views as auth_views

from django.urls import include ,path

from . import views

from .views import *



urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'registration/logged_outt.html'), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('patient/', views.HomeView.as_view(), name='liste-patient'),
    path('ajout_patient/', views.AjoutPatientList.as_view(), name='ajout_patient'),
    path('',PatientListAPIView.as_view(), name='api-view'),
    path('rdv/',RDVListAPIView.as_view(), name='ap-view'),
    path('habitude/',views.AjoutPatient.as_view(), name='habitude'),
    path('create/', create_rdv, name='create'),
    path('home/', views.home , name ="home"),
    path('<str:room>/', views.room , name ="room"),
    path('checkview/', views.checkview , name ="checkview"),
    path('send/', views.send , name ="send"),
    path('getMessages/<str:room>/', views.getMessages , name ="getMessages")
]