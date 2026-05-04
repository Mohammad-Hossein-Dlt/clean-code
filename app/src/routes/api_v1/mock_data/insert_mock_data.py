from ._router import router
from fastapi import HTTPException, Depends
from src.routes.http_response.responses import ResponseMessage
from src.repo.interface.Iuser_repo import IUserRepo
from src.repo.interface.Iwallet_repo import IWalletRepo
from src.repo.interface.Ipayout_repo import IPayoutRepo
from src.routes.depends.repo_depend import get_user_repo, get_wallet_repo, get_payout_repo
from src.domain.schemas.user.user_model import UserModel
from src.routes.depends.auth_depend import check_admin_access
from src.domain.mock_data.mock_data import mock_users, mock_wallets, mock_payouts
from src.usecases.mock_data.insert_mock_data import InsertMockData
from src.infra.exceptions.exceptions import AppBaseException

@router.post(
    "/",
    status_code=201,
    responses={
        **ResponseMessage.HTTP_401_UNAUTHORIZED("Authentication failed"),
        **ResponseMessage.HTTP_403_FORBIDDEN("Access denied"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }
)
async def insert_mock_payouts(
    user_repo: IUserRepo = Depends(get_user_repo),
    wallet_repo: IWalletRepo = Depends(get_wallet_repo),
    payout_repo: IPayoutRepo = Depends(get_payout_repo),
    admin: UserModel = Depends(check_admin_access),
):
    try:
        insert_mock_data_usecase = InsertMockData(user_repo, wallet_repo, payout_repo)
        return await insert_mock_data_usecase.execute(mock_users, mock_wallets, mock_payouts)
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))