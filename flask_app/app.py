"""
Main Flask application.
"""

from flask import Flask

from flask_app import db_url
from flask_app.db import db
from flask_app.db.init_db import initialize_database
from flask_app.api import api_bp


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(api_bp, url_prefix="/api")

with app.app_context():
    db.create_all()
    initialize_database()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
