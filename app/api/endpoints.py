from fastapi import APIRouter
import platform

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}

@router.get("/info", tags=["Info"])
async def info():
    return {
        "app": "Zimir",
        "version": "0.0.1",
        "platform": platform.platform(),
    }
