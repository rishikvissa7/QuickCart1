from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.category import Category
from schemas.category import CategoryCreate

# Category service functions for managing product categories
def get_all_categories(db: Session):
    return db.query(Category).all()


# Get a specific category by ID
def create_category(category: CategoryCreate, db: Session):
    if db.query(Category).filter(Category.name == category.name).first():
        raise HTTPException(status_code=400, detail="Category already exists")
    new_category = Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


# Update a specific category by ID
def update_category(category_id: int, category: CategoryCreate, db: Session):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    db_category.name = category.name
    db_category.description = category.description
    db.commit()
    db.refresh(db_category)
    return db_category


# Delete a specific category by ID
def delete_category(category_id: int, db: Session):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category)
    db.commit()
    return {"message": "Category deleted"}
