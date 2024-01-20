from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Patient(models.Model):
    
    SEX_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    
    SERVICE = (
        ('C', 'CHIRURGIEN'),
        ('CA', 'CARDIOLOGUE'),
        ('DER', 'DERMATOLOGUE'),
        ('DEN', 'DENTISTE'),
        ('O', 'OPHTALMOLOGUE'),
        ('dollar', 'dollar'),
        
    )
    
    
    
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)
    age = models.IntegerField(null=True)
    sexe = models.CharField(max_length=50, null=True)
    service = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
    
    
class HabitudeAlimentaire(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    jour = models.DateTimeField(auto_now_add=True)
    heure = models.TimeField(auto_now_add=True)
    repas = models.CharField(max_length=100)
    boisson = models.CharField(max_length=100)
    lieux = models.CharField(max_length=100)
    
class Room(models.Model):
    name = models.CharField(max_length=2000)
    date = models.DateField(auto_now_add=100)
    save_by = models.ForeignKey(User,on_delete=models.PROTECT)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    
class RendezVous(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=50)
    medecin = models.CharField(max_length=100)
    date = models.DateField()
    heure = models.TimeField()
    message = models.TextField(max_length=1000)
    
    