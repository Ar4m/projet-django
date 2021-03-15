## Projet Django

Pour lancer le projet :  
- Lancer la commande __"env\Scripts\activate"__ pour activer l'environnement virtuel
- Se placer dans le projet django_app et lancer la commande __"python manage.py runserver"__
- Aller sur __localhost:8000__

Le site est composé de différentes pages, qui sont en fait des templates auxquels on accède grâce aux views (après avoir défini les urls).  
Une de ces pages permet d'envoyer une candidature sous forme de formulaire, qui récupère les informations entrées et les sauvegarde dans la base de données à laquelle on accède en entrant "/admin" en fin d'url.