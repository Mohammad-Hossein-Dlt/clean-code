from fastapi import APIRouter

router = APIRouter(
    prefix="/mock-data",
    tags=["Mock data"]
)