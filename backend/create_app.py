from flask import Flask, session
from flask_migrate import Migrate

from blueprints.authentication import auth as auth_bp
from blueprints.api import api as api_bp
from database.models import db
from database.config import Config
from extensions import jwt


def create_app(app_name='VUESOC'):
    app = Flask(app_name)
    app.config.from_object(Config)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(api_bp, url_prefix="/api")
    db.init_app(app)

    jwt.init_app(app)

    migrate = Migrate(app, db)

    return app
