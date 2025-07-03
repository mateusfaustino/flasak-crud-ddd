from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class User:
    id: Optional[int] = None
    username: str = ""
    password_hash: str = ""


@dataclass
class Product:
    id: Optional[int] = None
    name: str = ""
    price: float = 0.0
    created_at: datetime = field(default_factory=datetime.utcnow)
