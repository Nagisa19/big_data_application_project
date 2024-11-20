"""
Initialize the database.
"""

import csv
from datetime import datetime

from flask_app.db import db
from flask_app.db.models import Etablissement

# CSV file path in Docker volume
CSV_FILE_PATH = '/docker-entrypoint-initdb.d/StockEtablissement_small.csv'


def load_data_from_csv():
    """
    Reads data from the CSV file and inserts it into the database if empty.
    """
    # Check if data already exists in the Etablissement table
    if db.session.query(db.func.count(Etablissement.siret)).scalar() == 0:
        with open(CSV_FILE_PATH, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = []

            for row in reader:
                # Map CSV columns to model fields
                mapped_row = {
                    'siren': row.get('siren'),
                    'nic': row.get('nic'),
                    'siret': row.get('siret'),
                    'statut_diffusion': row.get('statutDiffusionEtablissement'),
                    'date_creation': parse_date(row.get('dateCreationEtablissement')),
                    'tranche_effectifs': parse_int(row.get('trancheEffectifsEtablissement')),
                    'annee_effectifs': parse_int(row.get('anneeEffectifsEtablissement')),
                    'activite_principale_registre': row.get('activitePrincipaleRegistreMetiersEtablissement'),
                    'date_dernier_traitement': parse_datetime(row.get('dateDernierTraitementEtablissement')),
                    'etablissement_siege': parse_bool(row.get('etablissementSiege')),
                    'nombre_periodes': parse_int(row.get('nombrePeriodesEtablissement')),
                    'complement_adresse': row.get('complementAdresseEtablissement'),
                    'numero_voie': parse_int(row.get('numeroVoieEtablissement')),
                    'indice_repetition': row.get('indiceRepetitionEtablissement'),
                    'type_voie': row.get('typeVoieEtablissement'),
                    'libelle_voie': row.get('libelleVoieEtablissement'),
                    'code_postal': row.get('codePostalEtablissement'),
                    'libelle_commune': row.get('libelleCommuneEtablissement'),
                    'libelle_commune_etranger': row.get('libelleCommuneEtrangerEtablissement'),
                    'distribution_speciale': row.get('distributionSpecialeEtablissement'),
                    'code_commune': row.get('codeCommuneEtablissement'),
                    'code_cedex': row.get('codeCedexEtablissement'),
                    'libelle_cedex': row.get('libelleCedexEtablissement'),
                    'code_pays_etranger': row.get('codePaysEtrangerEtablissement'),
                    'libelle_pays_etranger': row.get('libellePaysEtrangerEtablissement'),
                    'complement_adresse2': row.get('complementAdresse2Etablissement'),
                    'numero_voie2': parse_int(row.get('numeroVoie2Etablissement')),
                    'indice_repetition2': row.get('indiceRepetition2Etablissement'),
                    'type_voie2': row.get('typeVoie2Etablissement'),
                    'libelle_voie2': row.get('libelleVoie2Etablissement'),
                    'code_postal2': row.get('codePostal2Etablissement'),
                    'libelle_commune2': row.get('libelleCommune2Etablissement'),
                    'libelle_commune_etranger2': row.get('libelleCommuneEtranger2Etablissement'),
                    'distribution_speciale2': row.get('distributionSpeciale2Etablissement'),
                    'code_commune2': row.get('codeCommune2Etablissement'),
                    'code_cedex2': row.get('codeCedex2Etablissement'),
                    'libelle_cedex2': row.get('libelleCedex2Etablissement'),
                    'code_pays_etranger2': row.get('codePaysEtranger2Etablissement'),
                    'libelle_pays_etranger2': row.get('libellePaysEtranger2Etablissement'),
                    'date_debut': parse_date(row.get('dateDebut')),
                    'etat_administratif': row.get('etatAdministratifEtablissement'),
                    'enseigne1': row.get('enseigne1Etablissement'),
                    'enseigne2': row.get('enseigne2Etablissement'),
                    'enseigne3': row.get('enseigne3Etablissement'),
                    'denomination_usuelle': row.get('denominationUsuelleEtablissement'),
                    'activite_principale': row.get('activitePrincipaleEtablissement'),
                    'nomenclature_activite_principale': row.get('nomenclatureActivitePrincipaleEtablissement'),
                    'caractere_employeur': row.get('caractereEmployeurEtablissement')
                }
                data.append(mapped_row)

            # Perform a bulk insert into the Etablissement table
            db.session.bulk_insert_mappings(Etablissement, data)
            db.session.commit()
            print("Data loaded successfully from CSV into the database.")


def parse_date(date_str):
    """
    Parses a date string and returns a datetime.date object.
    """
    if date_str:
        try:
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            pass  # Handle other date formats if necessary
    return None


def parse_datetime(datetime_str):
    """
    Parses a datetime string and returns a datetime.datetime object.
    """
    if datetime_str:
        try:
            return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            pass  # Handle other datetime formats if necessary
    return None


def parse_int(value):
    """
    Parses a string to an integer.
    """
    if value:
        try:
            return int(value)
        except ValueError:
            pass
    return None


def parse_bool(value):
    """
    Parses a string to a boolean.
    """
    if value is not None:
        return value.lower() in ('true', '1', 'yes', 'oui', 'o')
    return None


def initialize_database():
    """
    Initialize the database and load data if the Etablissement table is empty.
    """
    db.create_all()  # Create tables if they don't exist
    load_data_from_csv()  # Load data if table is empty
