from django.contrib import admin
from .models import *

# Register your models here.
class medecinAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'password')

class specialiteAdmin(admin.ModelAdmin):
    list_display = ('designation',)

class prescriptionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'age', 'sexe', 'email', 'antecedent','prescription1', 'prescription2', 'prescription3', 'Token')

class consultationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'age', 'service', 'sexe','status')

class AdminRDV(admin.ModelAdmin):
    list_display = ('nom','prenom','medecin', 'date', 'heure','message', 'status')

admin.site.register(Medecin, medecinAdmin)
admin.site.register(Specialite, specialiteAdmin)
admin.site.register(Prescription, prescriptionAdmin)
admin.site.register(Consultation, consultationAdmin)
admin.site.register(RendezVous,AdminRDV)
