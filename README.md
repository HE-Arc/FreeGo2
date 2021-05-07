# FreeGo2

Free Go est une association neuchâteloise à but non lucratif qui à comme objectifs d'aider les personnes en situations de précarité, ainsi que de diminuer le gaspillage alimentaire.

Pour ce faire, ils mettent à disposition des frigos, mis en place grâce à des soutiens (entreprises, privés, sponsors, etc.), où il est possible de donner les invendus ou de faire des dons alimentaires.

L'application développée dans le cadre de ce projet doit être une vitrine pour les frigos gérés par l'association. Les utilisateurs peuvent voir les positions et contenus des frigos, et les gestionnaires des frigos peuvent mettre à jour le contenu de leur frigo.

## Descrition de l'arborescence des fichiers du projet
L’arborescence des fichiers importants pour la compréhension de la structurede l’application est séparée en trois dossiers:backend/, freego/ et frontend/. backend/ contient tout ce qui est relatif à l’API. freego/ contient la configuration de Django avec notamment les fichiers .env et settings.py. frontend/ contient l’application Vue.js.

## Technologies et logiciels utilisés
- Django
- Django REST Framework
- Vue.js
- Vuetify
- Axios
- Google My Maps
- PostgreSQL
- Leaflet avec OpenStreetMap
- Visual Studio Code
- Python 3.9

## Procédure d'installation
```
git clone https://github.com/HE-Arc/FreeGo2.git
cd FreeGo2
pipenv path/to/your/python
pipenv install -r requirements
```
Il faut également installer [GDAL](https://gdal.org/download.html). La version 3.2.2 a été utilisée.
