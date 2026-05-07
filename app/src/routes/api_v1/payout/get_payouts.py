from ._router import router
from fastapi import Depends, HTTPException, Query
from src.routes.http_response.responses import ResponseMessage
from src.models.filter.payout_filter_input import PayoutFilterInput
from src.repo.interface.Iuser_repo import IUserRepo
from src.routes.depends.repo_depend import get_user_repo
from src.repo.interface.Ipayout_repo import IPayoutRepo
from src.routes.depends.repo_depend import get_payout_repo
from src.repo.interface.Iwallet_repo import IWalletRepo
from src.routes.depends.repo_depend import get_wallet_repo
from src.domain.schemas.user.user_model import UserModel
from src.routes.depends.auth_depend import check_admin_access
from src.usecases.payout.get_payouts import GetPayouts
from src.infra.exceptions.exceptions import AppBaseException

@router.get(
    "/get-all",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_401_UNAUTHORIZED("Authentication failed"),
        **ResponseMessage.HTTP_403_FORBIDDEN("Access denied"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }
)
async def all_payout(
    criteria: PayoutFilterInput = Query(None),
    user_repo: IUserRepo = Depends(get_user_repo),
    payout_repo: IPayoutRepo = Depends(get_payout_repo),
    wallet_repo: IWalletRepo = Depends(get_wallet_repo),
    admin: UserModel = Depends(check_admin_access)
):
    try:
        get_all_payouts_usecase = GetPayouts(user_repo, wallet_repo, payout_repo)
        output = await get_all_payouts_usecase.execute(criteria)
        return output.model_dump(mode="json")
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))