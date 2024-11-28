"""
Main Flask application.
"""

from flask import Flask
from flask_migrate import Migrate
from flask_app.db import db
from flask_app.api.routes import api_bp
from flask_app.db.init_db import initialize_database
from flask_app import db_url


def create_app() -> Flask:
    """
    Flask application factory.
    Creates and configures the Flask app instance.
    :return: a new Flask app instance.
    """
    flask_app = Flask(__name__)
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(flask_app)
    Migrate(flask_app, db)

    # Register blueprints
    flask_app.register_blueprint(api_bp, url_prefix="/api")

    # Run database initialization (if needed)
    with flask_app.app_context():
        initialize_database()

    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
