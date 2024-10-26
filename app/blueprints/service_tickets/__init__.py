from flask import Blueprint

loans_bp = Blueprint('serviceTickets_bp', __name__)

from . import routes