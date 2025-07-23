from fastapi import FastAPI
from routes import auth

app = FastAPI(title="Auth Service")
app.include_router(auth.router)
