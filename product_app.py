from fastapi import FastAPI
from routes import product

app = FastAPI(title="Product Service")
app.include_router(product.router)
