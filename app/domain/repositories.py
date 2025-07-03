"""Repository interface definitions for the domain layer."""

from typing import Iterable, Optional, Protocol

from .entities import Product, User


class UserRepositoryInterface(Protocol):
    """Interface for user persistence operations."""

    def get_by_username(self, username: str) -> Optional[User]:
        """Return a user by its username or ``None`` if not found."""

    def add(self, user: User) -> None:
        """Persist a ``User`` instance."""


class ProductRepositoryInterface(Protocol):
    """Interface for product persistence operations."""

    def all(self) -> Iterable[Product]:
        """Return all stored products."""

    def get(self, product_id: int) -> Optional[Product]:
        """Return a product by id or ``None`` if it does not exist."""

    def add(self, product: Product) -> None:
        """Persist a ``Product`` instance."""

    def delete(self, product: Product) -> None:
        """Remove a ``Product`` instance."""
