from fastapi import FastAPI
from routes import category

app = FastAPI(title="Category Service")
app.include_router(category.router)
