"""
Tests API endpoints.
"""

import unittest

import datetime

from flask import Flask

from flask_app.db.models import Etablissement, db
from flask_app.api import api_bp


class TestEtablissementAPI(unittest.TestCase):
    """
    Test cases for Etablissement API.
    """

    def setUp(self):
        """
        Set up a Flask app and database manually for testing.
        """
        # Manually set up the Flask app
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.app.config["TESTING"] = True

        # Initialize the database
        db.init_app(self.app)

        # Register the API blueprint
        self.app.register_blueprint(api_bp, url_prefix="/api")

        # Create a test client
        self.client = self.app.test_client()

        # Set up the database schema and add sample data
        with self.app.app_context():
            db.create_all()
            sample_etablissement = Etablissement(
                siren="123456789",
                nic="00012",
                siret="12345678900012",
                statut_diffusion="O",
                date_creation=datetime.date(2022, 1, 1),  # Use a datetime.date object
                tranche_effectifs=10,
                annee_effectifs=2022,
                activite_principale_registre="47.91Z",
                etablissement_siege=True,
                nombre_periodes=1,
                complement_adresse="Adresse complémentaire",
                numero_voie=10,
                libelle_voie="Rue Exemple",
                code_postal="75001",
                libelle_commune="Paris",
            )
            db.session.add(sample_etablissement)
            db.session.commit()

    def tearDown(self):
        """
        Tear down the database after each test.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_hello_world(self):
        """
        Test the /hello route.
        """
        response = self.client.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, World!"})

    def test_get_etablissements(self):
        """
        Test fetching a list of etablissements.
        """
        response = self.client.get('/api/etablissements')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['items']), 1)
        self.assertEqual(response.json['items'][0]['siret'], "12345678900012")

    def test_get_etablissement(self):
        """
        Test fetching a single etablissement by SIRET.
        """
        response = self.client.get('/api/etablissements/12345678900012')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['siret'], "12345678900012")

    def test_create_etablissement(self):
        """
        Test creating a new etablissement.
        """
        new_etablissement = {
            "siren": "987654321",
            "nic": "00098",
            "siret": "98765432100098",
            "statut_diffusion": "N",
            "date_creation": "2023-01-01",
            "tranche_effectifs": 5,
            "annee_effectifs": 2023,
            "activite_principale_registre": "56.10A",
            "etablissement_siege": False,
            "nombre_periodes": 2,
            "complement_adresse": "Test adresse",
            "numero_voie": 12,
            "libelle_voie": "Rue Test",
            "code_postal": "69001",
            "libelle_commune": "Lyon",
        }
        response = self.client.post('/api/etablissements', json=new_etablissement)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['siret'], "98765432100098")

    def test_update_etablissement(self):
        """
        Test updating an etablissement.
        """
        update_data = {
            "complement_adresse": "Nouvelle adresse complémentaire",
            "libelle_voie": "Nouvelle Rue Exemple",
        }
        response = self.client.put('/api/etablissements/12345678900012', json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['complement_adresse'], "Nouvelle adresse complémentaire")
        self.assertEqual(response.json['libelle_voie'], "Nouvelle Rue Exemple")

    def test_delete_etablissement(self):
        """
        Test deleting an etablissement.
        """
        response = self.client.delete('/api/etablissements/12345678900012')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Etablissement deleted")
        # Ensure it no longer exists
        response = self.client.get('/api/etablissements/12345678900012')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
