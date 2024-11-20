# Application of Big Data project

Projet application of Big Data M2.

# Présentation technique et gestion des systèmes.

## Organisation

![](./graphs/docker_organisation.png)

## Guide d'utilisation

- Ce projet est basé sur docker et docker-compose pour faciliter sa distribution.
- Il faut donc installer docker et docker-compose.
- Il faut ensuite créer les fichiers secrets dans la racine du projet :
    - ".env.postgres" :
      ```text
      POSTGRES_USER={my_user}
      POSTGRES_PASSWORD={my_password}
      POSTGRES_DB={my_db}
      ```
      
  - ".env.flask" :
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
- Elles peuvent être testées à l'aide des commandes curl suivantes :
    - Get a List of Etablissements :
    ```shell
    curl -X GET "http://localhost:5000/api/etablissements?page=1&per_page=10&sort=-date_creation&siret=00032517500016"
    ```
  
    - Get a Single Etablissement by SIRET :
    ```shell
    curl -X GET "http://localhost:5000/api/etablissements/00032517500016"
    ```

    - Create a New Etablissement :
    ```shell
    curl -X POST "http://localhost:5000/api/etablissements" \
    -H "Content-Type: application/json" \
    -d '{
      "siren": "123456789",
      "nic": "12345",
      "siret": "12345678912345",
      "statut_diffusion": "A",
      "date_creation": "2023-11-01",
      "tranche_effectifs": 50,
      "annee_effectifs": 2023,
      "activite_principale_registre": "Retail",
      "date_dernier_traitement": "2023-11-10T10:30:00",
      "etablissement_siege": true,
      "nombre_periodes": 2,
      "libelle_voie": "Main Street",
      "code_postal": "75001",
      "libelle_commune": "Paris",
      "code_commune": "75056",
      "activite_principale": "47.11Z",
      "nomenclature_activite_principale": "NAFRev2",
      "caractere_employeur": "O"
    }'
    ```

   - Update an Existing Etablissement :
   ```shell
   curl -X PUT "http://localhost:5000/api/etablissements/12345678912345" \
   -H "Content-Type: application/json" \
   -d '{
     "statut_diffusion": "B",
     "tranche_effectifs": 100
  }'
   ```
  
   - Delete an Etablissement :
   ```shell
   curl -X DELETE "http://localhost:5000/api/etablissements/12345678912345"
   ```
