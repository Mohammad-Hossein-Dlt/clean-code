from fastapi import APIRouter

router = APIRouter(
    prefix="/payout",
    tags=["Payout"]
)