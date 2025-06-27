from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from services import category as category_service
from services.auth import get_admin_user
from db.session import get_db
from schemas.category import CategoryCreate, CategoryShow
from models.user import User

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=List[CategoryShow])
def list_categories(db: Session = Depends(get_db)):
    return category_service.get_all_categories(db)

@router.post("/", response_model=CategoryShow)
def create_category(category: CategoryCreate, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    return category_service.create_category(category, db)

@router.put("/{category_id}", response_model=CategoryShow)
def update_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    return category_service.update_category(category_id, category, db)

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    return category_service.delete_category(category_id, db)
