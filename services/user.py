from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.user import User
from schemas.user import UserCreate
from services.auth import hash_password

# User service functions for managing users in the e-commerce application
def register_user(user: UserCreate, db: Session):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")

    if user.role == "admin":
        existing_admin = db.query(User).filter(User.role == "admin").first()
        if existing_admin:
            raise HTTPException(status_code=400, detail="Admin already exists")

    new_user = User(
        username=user.username,
        password=hash_password(user.password),
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# List all users
def list_users(db: Session):
    return db.query(User).all()


# Get a specific user by ID
def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Update a specific user by ID
def update_user(user_id: int, user_update: UserCreate, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.username = user_update.username
    db_user.password = hash_password(user_update.password)
    db_user.role = user_update.role
    db.commit()
    db.refresh(db_user)
    return db_user


# Delete a specific user by ID
def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}
