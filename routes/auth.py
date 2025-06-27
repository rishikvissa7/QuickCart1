from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from services import user as user_service
from services import auth as auth_service
from db.session import get_db
from schemas.user import UserCreate, UserShow, Token
from models.user import User

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserShow)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.register_user(user, db)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_service.get_user_by_username(db, form_data.username)
    if not user or not auth_service.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = auth_service.create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserShow)
def get_me(user: User = Depends(auth_service.get_current_user)):
    return user
