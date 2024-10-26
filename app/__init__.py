from flask import Flask
from app.models import db
from app.extensions import ma
from app.blueprints.customers.routes import customers_bp
from app.blueprints.service_tickets.routes import service_tickets_bp
from app.blueprints.mechanics.routes import mechanics_bp


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')

    # Add extensions
    db.init_app(app)
    ma.init_app(app)

    # Register blueprints
    app.register_blueprint(customers_bp, url_prefix="/customers")
    app.register_blueprint(service_tickets_bp, url_prefix="/service_tickets")
    app.register_blueprint(mechanics_bp, url_prefix="/mechanics")

    return app
