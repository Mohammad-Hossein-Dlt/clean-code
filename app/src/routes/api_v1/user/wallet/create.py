from ._router import router 
from fastapi import Depends, HTTPException
from src.routes.http_response.responses import ResponseMessage
from src.repo.interface.Iwallet_repo import IWalletRepo
from src.routes.depends.repo_depend import get_wallet_repo
from src.domain.schemas.user.user_model import UserModel
from src.routes.depends.auth_depend import get_authenticated_token_payload
from src.usecases.user.wallet.create import CreateWallet
from src.infra.exceptions.exceptions import AppBaseException

@router.post(
    "/",
    status_code=201,
    responses={
        **ResponseMessage.HTTP_401_UNAUTHORIZED("Authentication failed"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }
)
async def create_wallet(
    wallet_repo: IWalletRepo = Depends(get_wallet_repo),  
    user: UserModel = Depends(get_authenticated_token_payload),
):
    try:
        create_wallet_usecase = CreateWallet(wallet_repo)
        output = await create_wallet_usecase.execute(user.user_id)
        return output.model_dump(mode="json")
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))
