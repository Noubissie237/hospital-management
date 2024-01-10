from django.db import models

# Create your models here.
class Patient(models.Model):
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, unique=True, null=True)
    age = models.IntegerField(null=True)
    sexe = models.CharField(max_length=50)
    service = models.CharField(max_length=50)


    def __str__(self):
        return self.nom