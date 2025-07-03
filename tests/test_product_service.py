from datetime import datetime

from app.services.product_service import ProductService
from app.domain.entities import Product
from app.domain.repositories import ProductRepositoryInterface


class FakeProductRepository(ProductRepositoryInterface):
    def __init__(self):
        self.products = {}
        self.next_id = 1

    def all(self):
        return list(self.products.values())

    def get(self, product_id: int):
        return self.products.get(product_id)

    def add(self, product: Product) -> None:
        if product.id is None:
            product.id = self.next_id
            self.next_id += 1
            if product.created_at is None:
                product.created_at = datetime.utcnow()
        self.products[product.id] = Product(
            id=product.id,
            name=product.name,
            price=product.price,
            created_at=product.created_at,
        )

    def delete(self, product: Product) -> None:
        self.products.pop(product.id, None)


def test_product_crud_operations():
    repo = FakeProductRepository()
    service = ProductService(repo)

    product = service.create('Widget', 9.99)
    assert product.id == 1
    assert repo.get(product.id) == product
    assert len(repo.all()) == 1

    product = service.update(product, 'Gadget', 19.99)
    stored = repo.get(product.id)
    assert stored.name == 'Gadget'
    assert stored.price == 19.99

    service.delete(product)
    assert repo.all() == []
