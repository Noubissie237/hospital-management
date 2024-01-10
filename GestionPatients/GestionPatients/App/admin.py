from django.contrib import admin
from .models import Patient
# Register your models here.

class patientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'age', 'sexe', 'service')

admin.site.register(Patient, patientAdmin)