from flask import Blueprint

# Initialize the blueprint
auth = Blueprint('auth', __name__)

# Import the routes after the blueprint has been defined to avoid circular imports
from . import routes
