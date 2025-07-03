from ..domain.models import Product
from ..domain.repositories import ProductRepository


class ProductService:
    @staticmethod
    def create(name: str, price: float):
        product = Product(name=name, price=price)
        ProductRepository.add(product)
        return product

    @staticmethod
    def update(product: Product, name: str, price: float):
        product.name = name
        product.price = price
        ProductRepository.add(product)
        return product

    @staticmethod
    def get(product_id: int):
        return ProductRepository.get(product_id)

    @staticmethod
    def delete(product: Product):
        ProductRepository.delete(product)
