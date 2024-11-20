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
        db.Index('idx_siret', 'siret'),
        db.Index('idx_code_postal', 'code_postal')
    )

    def __init__(
            self, siren, nic, siret, statut_diffusion=None, date_creation=None, tranche_effectifs=None,
            annee_effectifs=None, activite_principale_registre=None, date_dernier_traitement=None,
            etablissement_siege=None, nombre_periodes=None, complement_adresse=None, numero_voie=None,
            indice_repetition=None, type_voie=None, libelle_voie=None, code_postal=None, libelle_commune=None,
            libelle_commune_etranger=None, distribution_speciale=None, code_commune=None, code_cedex=None,
            libelle_cedex=None, code_pays_etranger=None, libelle_pays_etranger=None, complement_adresse2=None,
            numero_voie2=None, indice_repetition2=None, type_voie2=None, libelle_voie2=None, code_postal2=None,
            libelle_commune2=None, libelle_commune_etranger2=None, distribution_speciale2=None, code_commune2=None,
            code_cedex2=None, libelle_cedex2=None, code_pays_etranger2=None, libelle_pays_etranger2=None,
            date_debut=None, etat_administratif=None, enseigne1=None, enseigne2=None, enseigne3=None,
            denomination_usuelle=None, activite_principale=None, nomenclature_activite_principale=None,
            caractere_employeur=None
    ):
        self.siren = siren
        self.nic = nic
        self.siret = siret
        self.statut_diffusion = statut_diffusion
        self.date_creation = date_creation
        self.tranche_effectifs = tranche_effectifs
        self.annee_effectifs = annee_effectifs
        self.activite_principale_registre = activite_principale_registre
        self.date_dernier_traitement = date_dernier_traitement
        self.etablissement_siege = etablissement_siege
        self.nombre_periodes = nombre_periodes
        self.complement_adresse = complement_adresse
        self.numero_voie = numero_voie
        self.indice_repetition = indice_repetition
        self.type_voie = type_voie
        self.libelle_voie = libelle_voie
        self.code_postal = code_postal
        self.libelle_commune = libelle_commune
        self.libelle_commune_etranger = libelle_commune_etranger
        self.distribution_speciale = distribution_speciale
        self.code_commune = code_commune
        self.code_cedex = code_cedex
        self.libelle_cedex = libelle_cedex
        self.code_pays_etranger = code_pays_etranger
        self.libelle_pays_etranger = libelle_pays_etranger
        self.complement_adresse2 = complement_adresse2
        self.numero_voie2 = numero_voie2
        self.indice_repetition2 = indice_repetition2
        self.type_voie2 = type_voie2
        self.libelle_voie2 = libelle_voie2
        self.code_postal2 = code_postal2
        self.libelle_commune2 = libelle_commune2
        self.libelle_commune_etranger2 = libelle_commune_etranger2
        self.distribution_speciale2 = distribution_speciale2
        self.code_commune2 = code_commune2
        self.code_cedex2 = code_cedex2
        self.libelle_cedex2 = libelle_cedex2
        self.code_pays_etranger2 = code_pays_etranger2
        self.libelle_pays_etranger2 = libelle_pays_etranger2
        self.date_debut = date_debut
        self.etat_administratif = etat_administratif
        self.enseigne1 = enseigne1
        self.enseigne2 = enseigne2
        self.enseigne3 = enseigne3
        self.denomination_usuelle = denomination_usuelle
        self.activite_principale = activite_principale
        self.nomenclature_activite_principale = nomenclature_activite_principale
        self.caractere_employeur = caractere_employeur
