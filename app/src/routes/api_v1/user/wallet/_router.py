from fastapi import APIRouter

router = APIRouter(
    prefix="/wallet",
    tags=["User wallet"],
)