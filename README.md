# Flask Framework Quickstart

07 - Accessing Request Data

https://flask.palletsprojects.com/en/2.2.x/quickstart/#accessing-request-data

Application réalisée avec Flask Framework sur la base de la documentation officielle https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application

## Environnement virtuel Python 

### Création
``
python3 -m venv env
``

### Activation

sur Unix : 

``
. env/bin/activate
``

ou sur Windows :

``
. env/Scripts/activate
``

### Désactivation de l'environnement virtuel

``
deactivate
``

## Installtion de Flask Framework

``
pip install flask
``

## Sauvegardes des dépendances du projet

``
pip freeze > requirements.txt
``

## Installtion des dépendances du projet 

(ex: après récupération du projet depuis un dépôt Git)

``
pip install -r requirements.txt
``

## Lancement de l'application Flask


``
flask --app hello run
``

La commande ci-dessus est fonctionnelle uniquement si le fichier principal de l'application se nomme hello.py

Sinon adapter la commande en remplaçant <hello> par le nom du fichier (sans l'extension .py)

L'application est (normalement) consultable sur http://localhost:5000

## Activation du mode Debug et du hot restart

``
flask --app hello --debug run
``

Le code PIN fourni dans la console Python permet d'exécuter du code directement dans la page du navigateur.