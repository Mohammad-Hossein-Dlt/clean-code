from ._router import router
from fastapi import Depends, HTTPException, Query
from app.src.routes.http_response.responses import ResponseMessage
from app.src.repo.interface.Ipayout_repo import IPayoutRepo
from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.routes.depends.payout_repo_depend import get_payout_repo
from app.src.routes.depends.user_repo_depend import get_user_repo
from app.src.routes.depends.auth_depend import check_admin_access
from app.src.domain.schemas.auth.jwt_payload import JWTPayload
from app.src.models.filter.payout_filter import PayoutFilter
from app.src.usecases.payout.get_all_payouts import GetAllPayouts
from app.src.infra.exceptions.exceptions import AppBaseException

@router.get(
    "/payouts",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_401_UNAUTHORIZED("Authentication failed"),
        **ResponseMessage.HTTP_403_FORBIDDEN("Access denied"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }
)
async def all_payout(
    payout_filter: PayoutFilter = Query(None),
    payout_repo: IPayoutRepo = Depends(get_payout_repo),
    user_repo: IUserRepo = Depends(get_user_repo),
    admin: JWTPayload = Depends(check_admin_access)
):
    try:
        get_all_payouts_usecase = GetAllPayouts(payout_repo, user_repo)
        return await get_all_payouts_usecase.execute(payout_filter)
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))