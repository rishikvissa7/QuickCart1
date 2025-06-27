from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from services import product as product_service
from services.auth import get_admin_user
from db.session import get_db
from schemas.product import ProductCreate, ProductShow
from models.user import User

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[ProductShow])
def list_products(
    category_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return product_service.list_products(db, category_id, skip, limit)

@router.get("/{product_id}", response_model=ProductShow)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.get_product(product_id, db)

@router.post("/", response_model=ProductShow)
def create_product(product: ProductCreate, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    return product_service.create_product(product, db)

@router.put("/{product_id}", response_model=ProductShow)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    return product_service.update_product(product_id, product, db)

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    return product_service.delete_product(product_id, db)
