from fastapi import FastAPI
from db.base import Base
from db.session import engine
from routes import auth, user, category, product

Base.metadata.create_all(bind=engine)

app = FastAPI(title="QuickCart")

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(category.router)
app.include_router(product.router)
