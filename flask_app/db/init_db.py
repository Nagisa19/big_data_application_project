"""
Initialize the database.
"""

import csv

from datetime import datetime, date

from flask_app.db import db
from flask_app.db.models import Etablissement

# CSV file path in Docker volume
CSV_FILE_PATH = '/docker-entrypoint-initdb.d/StockEtablissement.csv'


def load_data_from_csv() -> None:
    """
    Reads data from the CSV file and inserts it into the database row by row to avoid memory issues.
    :return: Nothing.
    """
    # Check if data already exists in the Etablissement table
    if db.session.query(db.func.count(Etablissement.siret)).scalar() == 0:
        print("Loading data row by row from CSV into the database.")
        with open(CSV_FILE_PATH, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Map CSV columns to model fields
                mapped_row = Etablissement(
                    siren=row.get('siren'),
                    nic=row.get('nic'),
                    siret=row.get('siret'),
                    statut_diffusion=row.get('statutDiffusionEtablissement'),
                    date_creation=parse_date(row.get('dateCreationEtablissement')),
                    tranche_effectifs=parse_int(row.get('trancheEffectifsEtablissement')),
                    annee_effectifs=parse_int(row.get('anneeEffectifsEtablissement')),
                    activite_principale_registre=row.get('activitePrincipaleRegistreMetiersEtablissement'),
                    date_dernier_traitement=parse_datetime(row.get('dateDernierTraitementEtablissement')),
                    etablissement_siege=parse_bool(row.get('etablissementSiege')),
                    nombre_periodes=parse_int(row.get('nombrePeriodesEtablissement')),
                    complement_adresse=row.get('complementAdresseEtablissement'),
                    numero_voie=parse_int(row.get('numeroVoieEtablissement')),
                    indice_repetition=row.get('indiceRepetitionEtablissement'),
                    type_voie=row.get('typeVoieEtablissement'),
                    libelle_voie=row.get('libelleVoieEtablissement'),
                    code_postal=row.get('codePostalEtablissement'),
                    libelle_commune=row.get('libelleCommuneEtablissement'),
                    libelle_commune_etranger=row.get('libelleCommuneEtrangerEtablissement'),
                    distribution_speciale=row.get('distributionSpecialeEtablissement'),
                    code_commune=row.get('codeCommuneEtablissement'),
                    code_cedex=row.get('codeCedexEtablissement'),
                    libelle_cedex=row.get('libelleCedexEtablissement'),
                    code_pays_etranger=row.get('codePaysEtrangerEtablissement'),
                    libelle_pays_etranger=row.get('libellePaysEtrangerEtablissement'),
                    complement_adresse2=row.get('complementAdresse2Etablissement'),
                    numero_voie2=parse_int(row.get('numeroVoie2Etablissement')),
                    indice_repetition2=row.get('indiceRepetition2Etablissement'),
                    type_voie2=row.get('typeVoie2Etablissement'),
                    libelle_voie2=row.get('libelleVoie2Etablissement'),
                    code_postal2=row.get('codePostal2Etablissement'),
                    libelle_commune2=row.get('libelleCommune2Etablissement'),
                    libelle_commune_etranger2=row.get('libelleCommuneEtranger2Etablissement'),
                    distribution_speciale2=row.get('distributionSpeciale2Etablissement'),
                    code_commune2=row.get('codeCommune2Etablissement'),
                    code_cedex2=row.get('codeCedex2Etablissement'),
                    libelle_cedex2=row.get('libelleCedex2Etablissement'),
                    code_pays_etranger2=row.get('codePaysEtranger2Etablissement'),
                    libelle_pays_etranger2=row.get('libellePaysEtranger2Etablissement'),
                    date_debut=parse_date(row.get('dateDebut')),
                    etat_administratif=row.get('etatAdministratifEtablissement'),
                    enseigne1=row.get('enseigne1Etablissement'),
                    enseigne2=row.get('enseigne2Etablissement'),
                    enseigne3=row.get('enseigne3Etablissement'),
                    denomination_usuelle=row.get('denominationUsuelleEtablissement'),
                    activite_principale=row.get('activitePrincipaleEtablissement'),
                    nomenclature_activite_principale=row.get('nomenclatureActivitePrincipaleEtablissement'),
                    caractere_employeur=row.get('caractereEmployeurEtablissement')
                )

                # Insert the row into the database
                db.session.add(mapped_row)

                # Commit periodically to reduce memory usage and prevent transaction bloat
                if reader.line_num % 1000 == 0:
                    print(f"Committing batch of rows up to line {reader.line_num}.")
                    db.session.commit()

            # Commit the remaining rows
            db.session.commit()
            print("Data loaded successfully row by row from CSV into the database.")


def parse_date(date_str: str) -> date | None:
    """
    Parses a date string into a datetime.date object.
    :param date_str: The date string to parse, formatted as 'YYYY-MM-DD'.
    :return: A datetime.date object representing the parsed date, or None if parsing fails.
    """
    if date_str:
        try:
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            pass  # Handle other date formats if necessary
    return None


def parse_datetime(datetime_str: str) -> date | None:
    """
    Parses a datetime string and returns a datetime.datetime object.
    :param datetime_str: The datetime string to parse, formatted as 'YYYY-MM-DDTHH:MM:SS'.
    :return: A datetime.datetime object representing the parsed datetime, or None if parsing fails.
    """
    if datetime_str:
        try:
            return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            pass  # Handle other datetime formats if necessary
    return None


def parse_int(value: str) -> int | None:
    """
    Parses a string to an integer.
    :param value: The string to parse as an integer.
    :return: An integer if the string can be parsed, otherwise None.
    """
    if value:
        try:
            return int(value)
        except ValueError:
            pass
    return None


def parse_bool(value: str) -> bool | None:
    """
    Parses a string into a boolean value.
    :param value: The string to parse as a boolean. Accepted values (case-insensitive) include:
                  'true', '1', 'yes', 'oui', 'o' for True.
                  Any other value will be considered False.
    :return: A boolean value (True or False), or None if the input is None.
    """
    if value is not None:
        return value.lower() in ('true', '1', 'yes', 'oui', 'o')
    return None


def initialize_database() -> None:
    """
    Initializes the database by creating all necessary tables and populating
    the data if the Etablissement table is empty.
    :return: nothing.
    """
    db.create_all()  # Create tables if they don't exist
    load_data_from_csv()  # Load data if table is empty
