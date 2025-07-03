from ..domain.entities import Product
from ..domain.repositories import ProductRepositoryInterface


class ProductService:
    """Business logic for products."""

    def __init__(self, product_repository: ProductRepositoryInterface) -> None:
        self.product_repository = product_repository

    def create(self, name: str, price: float):
        product = Product(name=name, price=price)
        self.product_repository.add(product)
        return product

    def update(self, product: Product, name: str, price: float):
        product.name = name
        product.price = price
        self.product_repository.add(product)
        return product

    def get(self, product_id: int):
        return self.product_repository.get(product_id)

    def delete(self, product: Product):
        self.product_repository.delete(product)
