import requests

API_ENDPOINT = 'http://127.0.0.1:8001/api/'

response = requests.get(API_ENDPOINT)
if response.status_code == 200:
    patients = response.json()
    for patient in patients:
        print(f"Name: {patient['nom']}")
        print(f"Age: {patient['age']}")
else:
    print("Erreur lors de la récupération des patients.")