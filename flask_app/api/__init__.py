"""
Initialization file for API.
"""

from flask import Blueprint

# Create the blueprint for API routes
api_bp = Blueprint('api', __name__)

# Import routes to associate them with the blueprint
from . import routes
