from ._router import router
from fastapi import Depends, HTTPException
from src.routes.http_response.responses import ResponseMessage
from src.models.schemas.user.update_user_input import UpdateUserInput
from src.repo.interface.Iwallet_repo import IWalletRepo
from src.routes.depends.repo_depend import get_wallet_repo
from src.domain.schemas.user.user_model import UserModel
from src.routes.depends.auth_depend import get_authenticated_token_payload
from src.usecases.user.wallet.update import UpdateWallet
from src.infra.exceptions.exceptions import AppBaseException


@router.put(
    "/",
    status_code=201,
    responses={
        **ResponseMessage.HTTP_401_UNAUTHORIZED("Authentication failed"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }    
)
async def update(
    entity: UpdateUserInput = Depends(),
    wallet_repo: IWalletRepo = Depends(get_wallet_repo),
    user: UserModel = Depends(get_authenticated_token_payload),
):
    try:
        login_user_usecase = UpdateWallet(wallet_repo)
        output = await login_user_usecase.execute(entity)
        return output.model_dump(mode="json")
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))
