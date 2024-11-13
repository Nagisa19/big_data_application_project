"""
API routes.
"""

from flask import jsonify

from flask_app.api import api_bp
from flask_app.db import db
from flask_app.db.models import Etablissement


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
    :return: a json saying "Hello, World!".
    """
    count = db.session.query(Etablissement).count()
    return jsonify({'count': count})