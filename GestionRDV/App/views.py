from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import PatientSerializer, RendezVousSerializer
from rest_framework import viewsets
from django.views import View
from requests.exceptions import RequestException
import requests
# Create your views here.

class RendezVousListAPIView(viewsets.ModelViewSet):
    queryset = RendezVous.objects.all()
    serializer_class = RendezVousSerializer


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    template_name= 'accounts/profile.html'
    habitude = HabitudeAlimentaire.objects.filter(user=request.user)
    
    
    context = {
        'session' : habitude,
    }
    
    print(context)
    
    return render(request, template_name,context)


class HomeView(View):
    
    templates_name = 'accounts/index.html'
    
    patient = Patient.objects.all()
    
    
    context = {
        'dossiers': patient
    }
    
    def get(self, request, *args, **kwags):
        return render(request, self.templates_name, self.context)

    def post(self, request, *args, **kwags):
        return render(request, self.templates_name, self.context)

class PatientListAPIView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

   
class AjoutPatient(LoginRequiredMixin,View):
    templates_name = 'accounts/ajout-habitude.html'
    
    def get(self, request, *args, **kwags):
        return render(request, self.templates_name)
    
    def post(self, request, *args, **kwags):
        
        data = {
            'jour': request.POST.get('jour'),
            'heure': request.POST.get('heure'),
            'repas': request.POST.get('repas'),
            'boisson': request.POST.get('boisson'),
            'lieux': request.POST.get('lieux'),
            'user': request.user

        }
        
        try:
            created = HabitudeAlimentaire.objects.create(**data)

            if created:

                print("enregistrer avec success")

            else:

                print("non enregistrer")
                
        except Exception as e:    
            
            print("Sorry our system is detecting the following issues {e}.")
         
        return render(request, self.templates_name)
    

def get_disponibilite_list():
    try:
        # Récupérer la liste des patients depuis le microservice Patient
        response = requests.get('http://gestionpersonnel:8000/api/dispo/')
        if response.status_code == 200:
            return response.json()
    except RequestException as e:
        print("Erreur lors de la récupération de la liste des patients :", str(e))
    return []

def create_rdv(request):
    if request.method == 'POST':
        nom = request.POST.get('name')
        prenom = request.POST.get('lastname')
        medecin = request.POST.get('nom-select')
        date = request.POST.get('date-select')
        heure = request.POST.get('heure-select')
        message = request.POST.get('message')
        rendezvous_obj = RendezVous(
            nom=nom,
            prenom=prenom,
            medecin=medecin,
            date=date,
            heure=heure,
            message=message,
        )
        rendezvous_obj.save()
    patient_list = get_disponibilite_list()
    print(patient_list)

    return render(request, 'accounts/prendre_rdv.html', {'patient_list': patient_list})

def home(request):
    return render(request, 'accounts/home.html')

def room(request , room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request , 'accounts/room.html' , {
        'username' : username ,
        'room' : room ,
        'room_details' : room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name = room).exists():
        return redirect('/'+ room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect('/'+ room + '/?username=' + username)
    

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value= message , user = username , room = room_id)
    new_message.save()
    return HttpResponse('Message envoyé avec succès')

def getMessages(request , room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room = room_details.id).order_by('date')
    return JsonResponse({"messages" :list(messages.values())})

class AjoutPatientList(View):
    templates_name = 'accounts/ajout_patient.html'
    
    def get(self, request, *args, **kwags):
        return render(request, self.templates_name)

    def post(self, request, *args, **kwags):
        
        data = {
            'nom': request.POST.get('name'),
            'prenom': request.POST.get('prenom'),
            'email': request.POST.get('email'),
            'sexe': request.POST.get('sex'),
            'age': request.POST.get('age'),
            'service': request.POST.get('service')

        }
        
        created = Patient.objects.create(**data)

        if created:

            print("patient creer avec success")
        else:

            print(" le patient n'as pas ete  creer ")

        
        return render(request, self.templates_name)
    
class AjoutRDV(View):
        
        templates_name = 'accounts/prendre_rdv.html'
        patient_list = get_disponibilite_list()
        print(patient_list)
    
        def get(self, request, *args, **kwags):
            return render(request, self.templates_name)

        def post(self, request, *args, **kwags):
        
            data = {
                'nom': request.POST.get('name'),
                'prenom': request.POST.get('lastname'),
                'medecin': request.POST.get('nom-select'),
                'date': request.POST.get('date-select"'),
                'heure': request.POST.get('heure-select'),
                'message': request.POST.get('message'),

            }
        
            created = RendezVous.objects.create(**data)

            if created:

                print("rdv creer avec success")
            else:

                print(" le rdv n'as pas ete  creer ")

            return render(request, 'accounts/prendre_rdv.html', {'patient_list': self.patient_list})

