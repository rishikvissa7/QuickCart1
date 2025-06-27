from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str]
    price: float
    stock: int
    category_id: int
    delete_check: bool

class ProductShow(ProductCreate):
    id: int

    class Config:
        from_attributes = True
