from .models import User, Product
from ..extensions import db


class UserRepository:
    @staticmethod
    def get_by_username(username: str):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def add(user: User):
        db.session.add(user)
        db.session.commit()


class ProductRepository:
    @staticmethod
    def all():
        return Product.query.all()

    @staticmethod
    def get(product_id: int):
        return Product.query.get(product_id)

    @staticmethod
    def add(product: Product):
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def delete(product: Product):
        db.session.delete(product)
        db.session.commit()
