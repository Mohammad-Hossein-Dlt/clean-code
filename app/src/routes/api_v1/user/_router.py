from fastapi import APIRouter
from .user._router import router as management_router
from .wallet._router import router as wallet_router

router = APIRouter(
    prefix="/user",
)

router.include_router(management_router)
router.include_router(wallet_router)