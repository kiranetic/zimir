from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(title="Zimir")

app.include_router(endpoints.router, prefix="/api")
