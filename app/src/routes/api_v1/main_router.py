from fastapi import APIRouter
from .user._router import router as user_router
from .mock_data._router import router as mock_data_router
from .payout._router import router as payout_router

ROUTE_PREFIX_VERSION_API = "/api_v1"

main_router_v1 = APIRouter()

main_router_v1.include_router(user_router, prefix=ROUTE_PREFIX_VERSION_API)
main_router_v1.include_router(mock_data_router, prefix=ROUTE_PREFIX_VERSION_API)
main_router_v1.include_router(payout_router, prefix=ROUTE_PREFIX_VERSION_API)
