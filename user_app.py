from fastapi import FastAPI
from routes import user

app = FastAPI(title="User Service")
app.include_router(user.router)
