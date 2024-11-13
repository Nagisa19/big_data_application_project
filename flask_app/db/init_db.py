"""
Initialize the database.
"""

import csv

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
            data = [row for row in reader]

            # Perform a bulk insert into the Etablissement table
            db.session.bulk_insert_mappings(Etablissement, data)
            db.session.commit()
            print("Data loaded successfully from CSV into the database.")

def initialize_database():
    """
    Initialize the database and load data if the Etablissement table is empty.
    """
    db.create_all()  # Create tables if they don't exist
    load_data_from_csv()  # Load data if table is empty