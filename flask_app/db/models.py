"""
Database models.
"""

import datetime

from typing import Optional

from sqlalchemy import event
from sqlalchemy.orm import Session

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
            self,
            siren: str,
            nic: str,
            siret: str,
            statut_diffusion: Optional[str] = None,
            date_creation: Optional[datetime.date] = None,
            tranche_effectifs: Optional[int] = None,
            annee_effectifs: Optional[int] = None,
            activite_principale_registre: Optional[str] = None,
            date_dernier_traitement: Optional[datetime] = None,
            etablissement_siege: Optional[bool] = None,
            nombre_periodes: Optional[int] = None,
            complement_adresse: Optional[str] = None,
            numero_voie: Optional[int] = None,
            indice_repetition: Optional[str] = None,
            type_voie: Optional[str] = None,
            libelle_voie: Optional[str] = None,
            code_postal: Optional[str] = None,
            libelle_commune: Optional[str] = None,
            libelle_commune_etranger: Optional[str] = None,
            distribution_speciale: Optional[str] = None,
            code_commune: Optional[str] = None,
            code_cedex: Optional[str] = None,
            libelle_cedex: Optional[str] = None,
            code_pays_etranger: Optional[str] = None,
            libelle_pays_etranger: Optional[str] = None,
            complement_adresse2: Optional[str] = None,
            numero_voie2: Optional[int] = None,
            indice_repetition2: Optional[str] = None,
            type_voie2: Optional[str] = None,
            libelle_voie2: Optional[str] = None,
            code_postal2: Optional[str] = None,
            libelle_commune2: Optional[str] = None,
            libelle_commune_etranger2: Optional[str] = None,
            distribution_speciale2: Optional[str] = None,
            code_commune2: Optional[str] = None,
            code_cedex2: Optional[str] = None,
            libelle_cedex2: Optional[str] = None,
            code_pays_etranger2: Optional[str] = None,
            libelle_pays_etranger2: Optional[str] = None,
            date_debut: Optional[datetime.date] = None,
            etat_administratif: Optional[str] = None,
            enseigne1: Optional[str] = None,
            enseigne2: Optional[str] = None,
            enseigne3: Optional[str] = None,
            denomination_usuelle: Optional[str] = None,
            activite_principale: Optional[str] = None,
            nomenclature_activite_principale: Optional[str] = None,
            caractere_employeur: Optional[str] = None
    ):
        """
        Initializes an instance of the class with detailed attributes.
        :param siren: The SIREN number of the entity.
        :param nic: The NIC (Numéro Interne de Classement) of the establishment.
        :param siret: The SIRET number (SIREN + NIC) of the establishment.
        :param statut_diffusion: Status of data dissemination (optional).
        :param date_creation: The creation date of the establishment (optional).
        :param tranche_effectifs: Range of employee counts (optional).
        :param annee_effectifs: Year of the employee count data (optional).
        :param activite_principale_registre: Main activity code in the registry (optional).
        :param date_dernier_traitement: Date of the last data update (optional).
        :param etablissement_siege: Indicates if the establishment is a headquarters (optional).
        :param nombre_periodes: Number of operational periods (optional).
        :param complement_adresse: Additional address details (optional).
        :param numero_voie: Street number (optional).
        :param indice_repetition: Repetition indicator (e.g., bis, ter) (optional).
        :param type_voie: Type of street (e.g., avenue, boulevard) (optional).
        :param libelle_voie: Street name (optional).
        :param code_postal: Postal code (optional).
        :param libelle_commune: Name of the city/town (optional).
        :param libelle_commune_etranger: City name (if located abroad) (optional).
        :param distribution_speciale: Special distribution information (optional).
        :param code_commune: City code (optional).
        :param code_cedex: CEDEX code (optional).
        :param libelle_cedex: CEDEX designation (optional).
        :param code_pays_etranger: Foreign country code (if applicable) (optional).
        :param libelle_pays_etranger: Foreign country name (if applicable) (optional).
        :param complement_adresse2: Additional address details for secondary location (optional).
        :param numero_voie2: Street number for secondary location (optional).
        :param indice_repetition2: Repetition indicator for secondary location (optional).
        :param type_voie2: Type of street for secondary location (optional).
        :param libelle_voie2: Street name for secondary location (optional).
        :param code_postal2: Postal code for secondary location (optional).
        :param libelle_commune2: City name for secondary location (optional).
        :param libelle_commune_etranger2: City name abroad for secondary location (optional).
        :param distribution_speciale2: Special distribution information for secondary location (optional).
        :param code_commune2: City code for secondary location (optional).
        :param code_cedex2: CEDEX code for secondary location (optional).
        :param libelle_cedex2: CEDEX designation for secondary location (optional).
        :param code_pays_etranger2: Foreign country code for secondary location (optional).
        :param libelle_pays_etranger2: Foreign country name for secondary location (optional).
        :param date_debut: Start date of activity (optional).
        :param etat_administratif: Administrative state/status of the entity (optional).
        :param enseigne1: First name of the establishment (optional).
        :param enseigne2: Second name of the establishment (optional).
        :param enseigne3: Third name of the establishment (optional).
        :param denomination_usuelle: Commonly used name of the establishment (optional).
        :param activite_principale: Main activity code (optional).
        :param nomenclature_activite_principale: Nomenclature of the main activity (optional).
        :param caractere_employeur: Indicates if the establishment is an employer (optional).
        """
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


class AuditLog(db.Model):
    """
    Audit table containing data about database transactions.
    """
    __tablename__ = 'audit_log'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    table_name = db.Column(db.String(255), nullable=False)
    operation = db.Column(db.String(10), nullable=False)  # INSERT, UPDATE, DELETE
    timestamp = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    row_data = db.Column(db.JSON, nullable=False)

    def __init__(self, table_name: str, operation: str, row_data: dict):
        """
        Initializes an instance of the class with detailed attributes.
        :param table_name: name of the affected table.
        :param operation: operation of the affected table.
        :param row_data: data sent to the affected table.
        """
        self.table_name = table_name
        self.operation = operation
        self.row_data = row_data


def serialize_row_data(row_data: dict) -> dict:
    """
    Serialize row data to make it JSON serializable.
    :param row_data: the data to serialize.
    :return: the serialized data.
    """
    def serialize(value: datetime.date | datetime.datetime | str) -> str:
        """
        Converts a datetime.date, datetime.datetime, or string value into a string format.
        :param value: The value to be serialized. It can be a datetime.date, datetime.datetime, or string.
        :type value: datetime.date | datetime.datetime | str
        :return: The serialized string representation of the input value.
        """
        if isinstance(value, (datetime.date, datetime.datetime)):
            return value.isoformat()
        return value

    return {key: serialize(value) for key, value in row_data.items()}


def record_audit_log(session: Session, operation: str, instance) -> None:
    """
    Helper function to record an audit log entry for database operations.
    :param session: The SQLAlchemy Session object to interact with the database.
    :param operation: The type of operation performed ('INSERT', 'UPDATE', 'DELETE').
    :param instance: The ORM-mapped instance representing the database record.
    :return: None
    """
    if isinstance(instance, AuditLog):
        # Skip logging for the AuditLog table itself
        return

    # Get the table name from the instance's class
    table_name = instance.__tablename__

    # Serialize the row data
    row_data = {}
    if operation == 'DELETE':
        # Collect data for delete operations
        row_data = {
            column.name: getattr(instance, column.name)
            for column in instance.__table__.columns
        }
    elif operation in {'INSERT', 'UPDATE'}:
        # Collect data for insert and update operations
        row_data = {
            column.name: getattr(instance, column.name)
            for column in instance.__table__.columns
        }

    # Serialize row_data to handle non-serializable objects
    serialized_row_data = serialize_row_data(row_data)

    # Create an AuditLog entry
    audit_entry = AuditLog(
        table_name=table_name,
        operation=operation,
        row_data=serialized_row_data
    )
    # Add the audit entry to the session
    session.add(audit_entry)


@event.listens_for(Session, "before_flush")
def before_flush(session: Session, flush_context, instances) -> None:
    """
    Event listener to handle auditing for insert, update, and delete operations before a flush.
    :param session: The SQLAlchemy Session instance initiating the flush.
    :param flush_context: Flush-specific context provided by SQLAlchemy (not used here).
    :param instances: Instances involved in the flush (not directly used here).
    :return: None
    """
    for instance in session.new:
        # Handle inserts
        record_audit_log(session, 'INSERT', instance)

    for instance in session.dirty:
        # Handle updates
        record_audit_log(session, 'UPDATE', instance)

    for instance in session.deleted:
        # Handle deletes
        record_audit_log(session, 'DELETE', instance)
