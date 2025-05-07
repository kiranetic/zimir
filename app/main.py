from fastapi import FastAPI
from app.db.init_db import init_db
from app.routes import endpoints
from app.users.router import router as user_endpoints

app = FastAPI(title="Zimir")

@app.on_event("startup")
async def startup_event():
    init_db()

app.include_router(endpoints.router, prefix="/api")

app.include_router(user_endpoints)
