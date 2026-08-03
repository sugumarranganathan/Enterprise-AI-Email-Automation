from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Enterprise AI Email Automation",
        "version": "1.0.0"
    }

@router.get("/")
def root():
    return {
        "message": "Enterprise AI Email Automation is running."
    }
