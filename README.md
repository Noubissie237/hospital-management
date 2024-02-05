# TP INF 331 GROUPE 20 :  Gestion d'un Hopital

# Application de Gestion d'un hopital en utilisant les langages de programmation Python, javaScript, et les framework Django et Bootstrap



## Equipes

* Superviseur: Dr AZANZI JIOMEKONG
* Chef de groupe: NOUBISSIE KAMGA WILFRIED  [lien vers son portfolio](https://noubissie237.github.io/)
 
* Développeurs
  * NDEUNA NGANA OUSMAN SINCLAIR: [lien vers son github](https://github.com/Nnos5)
  * DOLLAR MOHAMMED : [lien vers son github](https://github.com/vegapunk237/)
  * MOUNCHIGAM NFONTE HAMED : [lien vers son github](https://github.com/hamednfonte/)
  * TCHANKUIMEU MEUGHELA AMAELLE : [lien vers son github](https://github.com/MEUGHELA/)
  * NOUBISSIE KAMGA WILFRIED: [lien vers son github](https://github.com/Noubissie237/) 

## PRESENTATION DE L'APPLICATION
Dans le cadre de notre projet académique, nous avons entrepris la conception et le développement d'une application web dédiée à la gestion hospitalière. L'objectif principal de notre application est de fournir aux professionnels de la santé et aux administrateurs hospitaliers un outil complet et intuitif pour gérer efficacement les opérations quotidiennes d'un hôpital. L'application sera développée en utilisant **_Django_**
comme framework backend, **_Python_** pour la logique métier, **_JavaScript_** pour les fonctionnalités interactives côté client, et **_HTML_** **_CSS_** pour la présentation du contenu.


## 1. Fonctionnalités Requises
**a. Authentification Utilisateur** : Les utilisateurs doivent pouvoir se faire enrégistrer, se connecter et se déconnecter de l'application.

**b. Consultation et prescription** : L'application doit pouvoir permettre aux Docteurs de consulter les différents patients qui seront enregistrés.

**c. Achat de en ligne** : L'application doit permettre aux patients s'etant fait consulté de pouvoir faire des achats en ligne un site en ligne.

## 2. Interface Utilisateur
**a. Page de connexion** : Une première page permettant aux utilisateurs de se connecter uniquement

**b. Une page d'accueil** : Une page d'acceuil simple et fluide reservée uniquements aux médecins


## 3. Technologies Utilisées
L'application utilise les technologies suivantes :

**- Langage de Programmation**: Python  <br>
**- Framework Frontend** : Bootstrap_  <br>
**- Framework Backend** : _DJANGO_ <br>
**- Base de Données** : _SQLite_ <br>

# FONCTIONNEMENT

A partir du dossier racine, Demarrer le projet en tapant la commande: <br>
  - docker-compose up -d

Ouvrez chaque micro service dans le navigateur à l'adresse local et sur les ports ci-dessous: <br>

- Microservice de gestion des patients : port 8001
- Microservice de gestion du personnel : port 8000
- Microservice de gestion de la pharmacie : port 8002

## informations de connexion pour les microservice de gestion du personnel:
  - user : nom de la specialité (Exemple : Dentiste, Gynecologue, Ophtamologue, Generaliste, Chirurgiste)
  - password : admin