from ._router import router 
from fastapi import Depends, HTTPException
from app.src.routes.http_response.responses import ResponseMessage
from app.src.domain.schemas.auth.jwt_payload import JWTPayload
from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.routes.depends.auth_depend import get_authenticated_token_payload
from app.src.routes.depends.user_repo_depend import get_user_repo
from app.src.usecases.user.wallet.get_all_user_wallets import GetAllUserWallets
from app.src.infra.exceptions.exceptions import AppBaseException

@router.get(
    "/get-all",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_401_UNAUTHORIZED("Authentication failed"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }
)
async def get_all_user_wallets(
    user_repo: IUserRepo = Depends(get_user_repo),
    user: JWTPayload = Depends(get_authenticated_token_payload),
):
    try:
        get_wallet_usecase = GetAllUserWallets(user_repo)
        return await get_wallet_usecase.execute(user.user_id)
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))