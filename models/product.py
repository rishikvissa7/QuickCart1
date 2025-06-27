from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from db.base import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    price = Column(Float)
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))
    delete_check = Column(Boolean, default = True)
