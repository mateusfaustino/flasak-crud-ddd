"""Backward compatibility module for SQLAlchemy models."""

from ..adapters.sqlalchemy.models import User, Product

__all__ = ["User", "Product"]
