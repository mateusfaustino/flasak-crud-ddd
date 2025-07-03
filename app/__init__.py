from flask import Flask
from .config import Config
from .extensions import db, migrate, cors
from .controllers import register_controllers


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    register_controllers(app)

    return app
