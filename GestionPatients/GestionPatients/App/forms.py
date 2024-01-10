from django import forms

class PatientForm(forms.Form):
    nom = forms.CharField(max_length=50, required=False)
    prenom = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=True)
    age = forms.CharField(max_length=50, required=True)
    sexe = forms.CharField(max_length=50, required=True)
    service = forms.CharField(max_length=50, required=True)
