# Application of Big Data project

Project application of Big Data M2.

# Technichal presentation and systems managment.

## Organisation

![](./graphs/docker_organisation.png)

## Guide

- This project is based on docker and docker-compose to facilitate its distribution.
- Therefore, it is necessary to install docker and docker-compose.
- Then, you must create the secret files in the root of the project :
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
    
- To launch the full project, moove to the project's directory :
  ```shell
  cd big_data_application_project
  ```
  
- You must download the file [StockEtablissement_utf8.csv](https://efrei365net.sharepoint.com/:u:/r/sites/Section_2024-2025-A-ST2ABD-Groupe-DE2/Supports%20de%20cours/Datasets/API/StockEtablissement_utf8.zip?csf=1&web=1&e=Aa6HvX) and place it at the root of the project.
    - To simplify the test :
      ```shell
        head -n 1000 StockEtablissement_utf8.csv > StockEtablissement.csv
      ```
    - For the full version :  
      ```shell
      mv StockEtablissement_utf8.csv StockEtablissement.csv
      ```
- Then, to launch the services :
  ```shell
  docker-compose up -d --build
  ```

- To stop the services :
  ```shell
  docker-compose stop
  ```

- To stop the services and delete the containers and the volumes :
  ```shell
  docker-compose down
  ```

- Note that the volume used by the Postgres database survives the stops. If you want to start from scratch,
  Remove the volume:
  ```shell 
  docker volume rm big_data_application_project_postgres_data
  ```

- The test API is accessible at [http://localhost:5000/api/hello](http://localhost:5000/api/hello)
- They also can be tested with the following curl commands:
    - Hello World : 
    ```shell
    curl -X GET "http://localhost:5000/api/hello"
    ```
  
    - Check Data Base rows number :
    ```shell
    curl -X GET "http://localhost:5000/api/db_check"
    ```
  
    - Get a List of Etablissements with query :
    ```shell
    curl -X GET "http://localhost:5000/api/etablissements?page=1&per_page=10&sort=-date_creation"
  
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
