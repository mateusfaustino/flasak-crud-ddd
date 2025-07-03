from ...extensions import db
from .models import User as UserModel, Product as ProductModel
from ...domain.entities import User, Product
from ...domain.repositories import (
    UserRepositoryInterface,
    ProductRepositoryInterface,
)


class UserRepository(UserRepositoryInterface):
    """SQLAlchemy-backed user repository."""

    @staticmethod
    def get_by_username(username: str) -> User | None:
        result = UserModel.query.filter_by(username=username).first()
        if not result:
            return None
        return User(id=result.id, username=result.username, password_hash=result.password_hash)

    @staticmethod
    def add(user: User) -> None:
        if user.id is not None:
            model = UserModel.query.get(user.id)
            if model:
                model.username = user.username
                model.password_hash = user.password_hash
            else:
                model = UserModel(
                    id=user.id,
                    username=user.username,
                    password_hash=user.password_hash,
                )
                db.session.add(model)
        else:
            model = UserModel(
                username=user.username,
                password_hash=user.password_hash,
            )
            db.session.add(model)
        db.session.commit()
        user.id = model.id


class ProductRepository(ProductRepositoryInterface):
    """SQLAlchemy-backed product repository."""

    @staticmethod
    def all() -> list[Product]:
        products = ProductModel.query.all()
        return [
            Product(
                id=p.id,
                name=p.name,
                price=p.price,
                created_at=p.created_at,
            )
            for p in products
        ]

    @staticmethod
    def get(product_id: int) -> Product | None:
        p = ProductModel.query.get(product_id)
        if not p:
            return None
        return Product(
            id=p.id,
            name=p.name,
            price=p.price,
            created_at=p.created_at,
        )

    @staticmethod
    def add(product: Product) -> None:
        model = None
        if product.id is not None:
            model = ProductModel.query.get(product.id)
        if model:
            model.name = product.name
            model.price = product.price
        else:
            model = ProductModel(
                name=product.name,
                price=product.price,
                created_at=product.created_at,
            )
            db.session.add(model)
        db.session.commit()
        product.id = model.id
        product.created_at = model.created_at

    @staticmethod
    def delete(product: Product) -> None:
        model = ProductModel.query.get(product.id)
        if model:
            db.session.delete(model)
            db.session.commit()
