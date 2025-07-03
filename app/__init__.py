from flask import Flask
from flasgger import Swagger
from .config import Config
from .extensions import db, migrate, cors
from .controllers import register_controllers
from .adapters.sqlalchemy.repositories import UserRepository, ProductRepository
from .services.auth_service import AuthService
from .services.product_service import ProductService


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    Swagger(app)

    # Set up repositories and services
    user_repo = UserRepository()
    product_repo = ProductRepository()
    app.auth_service = AuthService(user_repo)
    app.product_service = ProductService(product_repo)

    register_controllers(app)

    return app
