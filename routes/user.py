from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from services import user as user_service
from services import auth as auth_service
from db.session import get_db
from schemas.user import UserCreate, UserShow
from models.user import User

router = APIRouter(prefix="/auth/user", tags=["Users"])

@router.get("/admin/users", response_model=List[UserShow])
def list_users(db: Session = Depends(get_db), admin: User = Depends(auth_service.get_admin_user)):
    return user_service.list_users(db)

@router.get("/admin/users/{user_id}", response_model=UserShow)
def get_user(user_id: int, db: Session = Depends(get_db), admin: User = Depends(auth_service.get_admin_user)):
    return user_service.get_user_by_id(user_id, db)

@router.put("/admin/users/{user_id}", response_model=UserShow)
def update_user(user_id: int, user_update: UserCreate, db: Session = Depends(get_db), admin: User = Depends(auth_service.get_admin_user)):
    return user_service.update_user(user_id, user_update, db)

@router.delete("/admin/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), admin: User = Depends(auth_service.get_admin_user)):
    return user_service.delete_user(user_id, db)
