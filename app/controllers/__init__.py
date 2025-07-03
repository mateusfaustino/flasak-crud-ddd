from .auth_controller import auth_bp
from .product_controller import product_bp


def register_controllers(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp, url_prefix='/products')
