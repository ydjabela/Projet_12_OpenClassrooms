# Projet_12_OpenClassrooms
## Créez une API sécurisée RESTful en utilisant Django REST
Epic Events, une entreprise de conseil et de gestion dans l'événementiel qui répond aux besoins des start-up voulant organiser des « fêtes épiques ».

###Description du projet :
Démonstration de l'application opérationnelle de CRM Django finale.
* Le code d'une application présentant des points de terminaison d'API sécurisés utilisant le framework Django REST pour permettre les opérations CRUD et le site d'administration Django en tant qu'interface front-end.
* Django ORM & une base de données PostgreSQL configurés dans le fichier « settings.py ».

### Récupérer le projet :

```
git clone https://github.com/ydjabela/Projet_12_Openclassrooms
```

### Création de l'environnement virtuel

Assurez-vous d'avoir installé python et de pouvoir y accéder via votre terminal, en ligne de commande.

Si ce n'est pas le cas : https://www.python.org/downloads/

```
python -m venv Projet_12
```

### Activation de l'environnement virtuel du projet

Windows :

```
Projet_12\Scripts\activate.bat
```

MacOS/Linux :
```
source Projet_12/bin/activate
```

### Installation des packages necessaire pour ce projet
```
pip install -r requirements.txt
```

### Fonctionnement:
Une fois activé, pour démarrer le serveur local, il faudra utiliser la commande :
```
python manage.py runserver 
```
### Postman documentation

Suivre les  indications detaillé dans le site suivant:
https://documenter.getpostman.com/view/21236516/VUxNQ7dj
#### Cette commande sera obligatoire à chaque fois que vous voudrez travailler avec le cours. Dans le même terminal, tapez maintenant
```
pip install -r requirements.txt
```
###Vérifier la qualité du code :
Pour lancer la vérification de la qualité du code : 
```
flake8 --format=html --htmldir=flake-report --exclude=env --max-line-length=119
```
### Contributeurs
- Yacine Djabela
- Stephane Didier



cd OneDrive
cd Documents
cd GitHub
Projet_12\Scripts\activate.bat
cd Projet_12_OpenClassrooms
cd Epicevents
python manage.py runserver 
