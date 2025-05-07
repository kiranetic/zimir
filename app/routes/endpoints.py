from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}

@router.get("/info", tags=["Info"])
def get_info():
    return {
        "app": "Zimir",
        "version": "0.0.1"
    }
