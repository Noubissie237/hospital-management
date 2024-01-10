from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
from django.http import HttpResponseRedirect

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


# Create your views here.
def home(request):
    
    world = ""

    if request.method == 'POST':
        
        data = request.POST

        try:

            pushit = Patient(nom=data['nom'], prenom=data['prenom'], email=data['email'], age=data['age'], sexe=data['sexe'], service=data['service'])
            
            pushit.save()

            print('Sauvegarde Réussi')

            world = "Enregistrement effectué avec succèss"

        except:

            world = "Echec d'enregistrement, cet adresse mail existe déjà"


        return render(request, 'index.html', context={'message' : world})

    else:

        return render(request, 'index.html', context={'message' : world})