"""Category model for the e-commerce application."""
from sqlalchemy import Column, Integer, String
from db.base import Base

"""This model represents product categories in the application."""
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
