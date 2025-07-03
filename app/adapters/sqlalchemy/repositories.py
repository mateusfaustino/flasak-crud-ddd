from ...extensions import db
from .models import User, Product
from ...domain.repositories import (
    UserRepositoryInterface,
    ProductRepositoryInterface,
)


class UserRepository(UserRepositoryInterface):
    """SQLAlchemy-backed user repository."""

    @staticmethod
    def get_by_username(username: str) -> User | None:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def add(user: User) -> None:
        db.session.add(user)
        db.session.commit()


class ProductRepository(ProductRepositoryInterface):
    """SQLAlchemy-backed product repository."""

    @staticmethod
    def all() -> list[Product]:
        return Product.query.all()

    @staticmethod
    def get(product_id: int) -> Product | None:
        return Product.query.get(product_id)

    @staticmethod
    def add(product: Product) -> None:
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def delete(product: Product) -> None:
        db.session.delete(product)
        db.session.commit()
