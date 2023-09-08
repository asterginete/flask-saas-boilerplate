from flask import Blueprint

# Initialize the blueprint
billing = Blueprint('billing', __name__)

# Import the routes after the blueprint has been defined to avoid circular imports
from . import routes
