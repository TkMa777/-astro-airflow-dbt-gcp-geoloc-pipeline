# Traitement des données avec Airflow, DBT et GCP sur Astro

Ce projet illustre l'intégration et l'orchestration de divers outils et plateformes dans le domaine de l'ingénierie des données pour fournir une solution complète de traitement et d'analyse de données. En combinant Airflow, DBT et GCP au sein d'Astro, ce projet offre une approche robuste et évolutive pour gérer les workflows de données, depuis l'acquisition et le traitement jusqu'à l'analyse et la visualisation. Voici quelques-uns des aspects clés du projet :

- **Orchestration avec Airflow :** Utilisation d'Apache Airflow pour orchestrer et planifier les workflows de données, permettant ainsi une gestion automatisée et bien structurée des tâches de traitement de données.

- **Transformation des données avec DBT :** Emploi de DBT pour effectuer des transformations de données complexes et efficaces, garantissant que les données sont préparées et optimisées pour l'analyse.

- **Stockage et traitement dans le cloud avec GCP :** Utilisation des services de stockage et de calcul de Google Cloud Platform pour héberger et exécuter les processus de données, assurant une élasticité et une puissance de calcul adaptées aux besoins du projet.

- **Déploiement sur Astro :** Le projet est déployé sur Astro, ce qui facilite l'exécution et la gestion des workflows Airflow dans un environnement cloud, offrant ainsi une scalabilité et une maintenance réduites.

En somme, ce projet vise à démontrer comment les technologies modernes d'ingénierie des données peuvent être intégrées pour construire des pipelines de données efficaces et évolutifs, capables de soutenir des décisions basées sur des données précises et pertinentes.


## Vue d'ensemble
Ce dépôt contient les workflows de traitement des données pour un projet qui utilise Apache Airflow pour l'orchestration, DBT (Data Build Tool) pour la transformation des données, et Google Cloud Platform (GCP) pour les services cloud. Le projet est conçu pour fonctionner sur Astro, qui fournit un environnement basé sur le cloud pour Airflow.

## Fonctionnalités
- **DAGs Airflow** : Graphes acycliques dirigés pour l'orchestration des pipelines de données.
- **Modèles DBT** : Transformations basées sur SQL pour structurer et optimiser les données pour l'analytique.
- **Intégration GCP** : Utilisation des services GCP pour le stockage des données évolutif et le traitement.


## Prérequis
- Docker
- CLI Astro
- Compte GCP

## Installation
Pour configurer l'environnement de ce projet, suivez ces étapes :

1. Clonez le dépôt :
    git clone <URL-du-dépôt>


2. Naviguez vers le répertoire du projet :


3. Installez la CLI Astro en suivant les instructions sur [la documentation d'Astro](https://www.astronomer.io/docs/).

4. Authentifiez-vous auprès de GCP et configurez les services requis (Storage, BigQuery, etc.).

5. Construisez l'image Docker :
    docker build -t <nom-de-votre-image> .


6. Initialisez un projet Astro si cela n'a pas encore été fait :
     astro dev init


7. Démarrez l'environnement :
    astro dev start



## Utilisation
Déployez les workflows dans l'environnement Astro et surveillez vos tâches de traitement des données via l'interface utilisateur Airflow.

Pour exécuter les commandes DBT, utilisez :
    dbt run
    dbt test


## Contribution
Nous accueillons les contributions ! Veuillez lire `CONTRIBUTING.md` pour les détails sur comment contribuer à ce projet.

## Licence
Ce projet est sous licence [MIT License](LICENSE).
