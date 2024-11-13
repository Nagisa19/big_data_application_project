# Application of Big Data project

Projet application of Big Data M2.

# Présentation technique et gestion des systèmes.

## Organisation

![](./graphs/docker_organisation.png)

## Guide d'utilisation

- Ce projet est basé sur docker et docker-compose pour faciliter sa distribution.
- Il faut donc installer docker et docker-compose.
- Il faut ensuite créer les fichiers secrets dans la racine du projet :
    - ".env.postgres":
      ```text
      POSTGRES_USER={my_user}
      POSTGRES_PASSWORD={my_password}
      POSTGRES_DB={my_db}
      ```
      
  - ".env.flask":
      ```text
      FLASK_ENV=development
      DATABASE_URL=postgresql://{my_user}:{my_password}@flask_db:5432/{my_db}
      ```
    
- Pour lancer le projet complet, on se déplace dans le répertoire du projet :
  ```shell
  cd big_data_application_project
  ```
  
- Puis :
  ```shell
  docker-compose up -d --build
  ```

- Pour arrêter tous les services :
  ```shell
  docker-compose stop
  ```

- Pour arrêter les services et supprimer les conteneurs et les volumes :
  ```shell
  docker-compose down
  ```

- Il est à noter que le volume utilisé par la base de données Postgres survit aux arrêts. Si on veut repartir de zéro,
  il faut supprimer le volume :
  ```shell 
  docker volume rm big_data_application_project_postgres_data
  ```

- L'API de test est accessible à l'adresse [http://localhost:5000/api/hello](http://localhost:5000/api/hello)
