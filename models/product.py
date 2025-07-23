"""Product model for the e-commerce application."""
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db.base import Base


"""This model represents products in the application."""
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    price = Column(Float)
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))
