"""
API routes.
"""

from flask import request, jsonify, abort
from flask_app.api import api_bp
from flask_app.db import db
from flask_app.db.models import Etablissement

from sqlalchemy import inspect


def etablissement_to_dict(etablissement):
    """
    Helper function to convert Etablissement objects to dictionaries
    :param etablissement: instance of an etablissement.
    :return: dictionnary representation of the etablissement.
    """
    inspector = inspect(etablissement)
    return {column.key: getattr(etablissement, column.key) for column in inspector.mapper.column_attrs}


@api_bp.route("/hello", methods=["GET"])
def hello_world():
    """
    Test API.
    :return: a json saying "Hello, World!".
    """
    return jsonify({"message": "Hello, World!"})


@api_bp.route("/db_check", methods=["GET"])
def count_establishments():
    """
    Test DB.
    :return: a json with the count of Etablissements.
    """
    count = Etablissement.query.count()
    return jsonify({'count': count})


@api_bp.route("/etablissements", methods=["GET"])
def get_etablissements():
    """
    Get a list of Etablissements with optional filters, sorting, and pagination.
    :return: a list of etablissements.
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    query = Etablissement.query

    # List of valid fields for filtering and sorting
    inspector = inspect(Etablissement)
    valid_fields = [column.key for column in inspector.mapper.column_attrs]

    # Implement filters
    filter_args = {}
    for field in valid_fields:
        value = request.args.get(field)
        if value:
            filter_args[field] = value

    if filter_args:
        query = query.filter_by(**filter_args)

    # Implement sorting
    sort = request.args.get('sort')
    if sort:
        sort_fields = []
        for field in sort.split(','):
            desc = False
            if field.startswith('-'):
                desc = True
                field = field[1:]
            if field in valid_fields:
                column_attr = getattr(Etablissement, field)
                if desc:
                    column_attr = column_attr.desc()
                sort_fields.append(column_attr)
            else:
                abort(400, description=f"Invalid sort field: {field}")
        if sort_fields:
            query = query.order_by(*sort_fields)

    # Implement pagination
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    items = [etablissement_to_dict(e) for e in pagination.items]

    return jsonify({
        'total': pagination.total,
        'pages': pagination.pages,
        'page': page,
        'per_page': per_page,
        'items': items
    })


@api_bp.route("/etablissements/<string:siret>", methods=["GET"])
def get_etablissement(siret):
    """
    Get an Etablissement by SIRET.
    :param siret: the siret number of the etablissement to retrieve.
    :return: a json containing the wanted etablissement.
    """
    etablissement = Etablissement.query.get(siret)
    if etablissement is None:
        abort(404, description="Etablissement not found")
    return jsonify(etablissement_to_dict(etablissement))


@api_bp.route("/etablissements", methods=["POST"])
def create_etablissement():
    """
    Create a new Etablissement. The fields 'siret', 'siren' and 'nic' are required.
    :return: a json containing the created etablissement or an error message.
    """
    data = request.get_json()
    if not data:
        abort(400, description="No input data provided")

    # Ensure obligatory is provided
    required_fields = ['siret', 'siren', 'nic']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        abort(400, description=f"Missing required field(s): {', '.join(missing_fields)}")

    # Check if Etablissement with the same SIRET already exists
    existing_etablissement = Etablissement.query.get(data['siret'])
    if existing_etablissement:
        abort(400, description="Etablissement with this SIRET already exists")

    # Create an Etablissement object from data
    etablissement = Etablissement(**data)

    try:
        db.session.add(etablissement)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(400, description=f"Error creating Etablissement: {e}")

    return jsonify(etablissement_to_dict(etablissement)), 201


@api_bp.route("/etablissements/<string:siret>", methods=["PUT"])
def update_etablissement(siret):
    """
    Update an existing Etablissement.
    - Allows modification of fields except for 'siret', 'siren', and 'nic'.
    :param siret: the siret number of the etablissment to update.
    :return: a json containing the updated etablissement or an error message.
    """
    etablissement = Etablissement.query.get(siret)
    if etablissement is None:
        abort(404, description="Etablissement not found")

    data = request.get_json()
    if not data:
        abort(400, description="No input data provided")

    # Prevent changing the obligatory fields
    unmodifiable_fields = ['siret', 'siren', 'nic']
    for field in unmodifiable_fields:
        if field in data:
            abort(400, description=f"Cannot change the '{field}' of an Etablissement")

    # Update fields
    inspector = inspect(Etablissement)
    valid_fields = [column.key for column in inspector.mapper.column_attrs]
    for key, value in data.items():
        if key in valid_fields:
            setattr(etablissement, key, value)
        else:
            abort(400, description=f"Invalid field: {key}")

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(400, description=f"Error updating Etablissement: {e}")

    return jsonify(etablissement_to_dict(etablissement))


@api_bp.route("/etablissements/<string:siret>", methods=["DELETE"])
def delete_etablissement(siret):
    """
     Delete an Etablissement by giving the siret number of the Etablissement to delete.
    :param siret: the siret number of the etablissment to delete.
    :return: a message confirming the deletion or an error message.
    """
    etablissement = Etablissement.query.get(siret)
    if etablissement is None:
        abort(404, description="Etablissement not found")

    try:
        db.session.delete(etablissement)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(400, description=f"Error deleting Etablissement: {e}")

    return jsonify({"message": "Etablissement deleted"})
