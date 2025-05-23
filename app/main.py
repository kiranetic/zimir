from fastapi import FastAPI
from app.db.init_db import init_db
from app.routes.endpoints import router as system_router
from app.auth.router import router as auth_router
from app.users.router import router as user_router
from app.categories.router import router as category_router
from app.transactions.router import router as transaction_router

app = FastAPI(title="Zimir")

@app.on_event("startup")
async def startup_event():
    init_db()

app.include_router(system_router, prefix="/api")
app.include_router(auth_router, prefix="/login")
app.include_router(user_router)
app.include_router(category_router)
app.include_router(transaction_router)
