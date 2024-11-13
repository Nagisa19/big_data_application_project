"""
Database models.
"""

from flask_app.db import db


class Etablissement(db.Model):
    """
    Database model for Etablissement.
    """
    __tablename__ = 'etablissement'

    siren = db.Column(db.String(9), nullable=False)
    nic = db.Column(db.String(5), nullable=False)
    siret = db.Column(db.String(14), primary_key=True)
    statut_diffusion = db.Column(db.String(1))
    date_creation = db.Column(db.Date)
    tranche_effectifs = db.Column(db.Integer)
    annee_effectifs = db.Column(db.Integer)
    activite_principale_registre = db.Column(db.String(255))
    date_dernier_traitement = db.Column(db.DateTime)
    etablissement_siege = db.Column(db.Boolean)
    nombre_periodes = db.Column(db.Integer)
    complement_adresse = db.Column(db.String(255))
    numero_voie = db.Column(db.Integer)
    indice_repetition = db.Column(db.String(10))
    type_voie = db.Column(db.String(5))
    libelle_voie = db.Column(db.String(255))
    code_postal = db.Column(db.String(10))
    libelle_commune = db.Column(db.String(255))
    libelle_commune_etranger = db.Column(db.String(255))
    distribution_speciale = db.Column(db.String(255))
    code_commune = db.Column(db.String(5))
    code_cedex = db.Column(db.String(10))
    libelle_cedex = db.Column(db.String(255))
    code_pays_etranger = db.Column(db.String(5))
    libelle_pays_etranger = db.Column(db.String(255))
    complement_adresse2 = db.Column(db.String(255))
    numero_voie2 = db.Column(db.Integer)
    indice_repetition2 = db.Column(db.String(10))
    type_voie2 = db.Column(db.String(5))
    libelle_voie2 = db.Column(db.String(255))
    code_postal2 = db.Column(db.String(10))
    libelle_commune2 = db.Column(db.String(255))
    libelle_commune_etranger2 = db.Column(db.String(255))
    distribution_speciale2 = db.Column(db.String(255))
    code_commune2 = db.Column(db.String(5))
    code_cedex2 = db.Column(db.String(10))
    libelle_cedex2 = db.Column(db.String(255))
    code_pays_etranger2 = db.Column(db.String(5))
    libelle_pays_etranger2 = db.Column(db.String(255))
    date_debut = db.Column(db.Date)
    etat_administratif = db.Column(db.String(1))
    enseigne1 = db.Column(db.String(255))
    enseigne2 = db.Column(db.String(255))
    enseigne3 = db.Column(db.String(255))
    denomination_usuelle = db.Column(db.String(255))
    activite_principale = db.Column(db.String(10))
    nomenclature_activite_principale = db.Column(db.String(50))
    caractere_employeur = db.Column(db.String(1))

    # Define indexes
    __table_args__ = (
        db.Index('idx_siren', 'siren'),
        db.Index('idx_nic', 'nic'),
        db.Index('idx_code_postal', 'code_postal'),
        db.Index('idx_libelle_commune', 'libelle_commune'),
    )
