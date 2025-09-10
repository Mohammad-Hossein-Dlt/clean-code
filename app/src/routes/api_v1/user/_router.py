from fastapi import APIRouter
from app.src.routes.api_v1.user.user._router import router as management_router
from app.src.routes.api_v1.user.wallet._router import router as wallet_router

router = APIRouter(
    prefix="/user",
)

router.include_router(management_router)
router.include_router(wallet_router)