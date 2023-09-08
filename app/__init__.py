from flask import Blueprint

# Initialize the blueprint
main = Blueprint('main', __name__)

# Import the routes after the blueprint has been defined to avoid circular imports
from . import routes
