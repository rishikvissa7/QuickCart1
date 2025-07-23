from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Optional
from models.product import Product
from schemas.product import ProductCreate


# Product service functions for managing products in the e-commerce application
def list_products(db: Session, category_id: Optional[int] = None, skip: int = 0, limit: int = 10):
    query = db.query(Product)
    if category_id:
        query = query.filter(Product.category_id == category_id)
    return query.offset(skip).limit(limit).all()


# Get a specific product by ID
def get_product(product_id: int, db: Session):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# Create a new product
def create_product(product: ProductCreate, db: Session):
    new_product = Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


# Update a specific product by ID
def update_product(product_id: int, product: ProductCreate, db: Session):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for attr, value in product.model_dump().items():
        setattr(db_product, attr, value)
    db.commit()
    db.refresh(db_product)
    return db_product


# Delete a specific product by ID
def delete_product(product_id: int, db: Session):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.delete_check = True
    db.commit()
    return {"message": "Product deleted"}
