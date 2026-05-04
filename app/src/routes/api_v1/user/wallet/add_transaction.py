from ._router import router
from fastapi import Depends, HTTPException
from src.routes.http_response.responses import ResponseMessage
from src.models.schemas.user.user_transaction_input import UserTransactionInput
from src.repo.interface.Iwallet_repo import IWalletRepo
from src.routes.depends.repo_depend import get_wallet_repo
from src.domain.schemas.user.user_model import UserModel
from src.routes.depends.auth_depend import get_authenticated_token_payload
from src.usecases.user.wallet.add_transaction import AddTransaction 
from src.infra.exceptions.exceptions import AppBaseException

@router.post(
    "/transaction",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_401_UNAUTHORIZED("Authentication failed"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }
)
async def add_transaction(
    wallet_id: str,
    transaction: UserTransactionInput = Depends(),
    wallet_repo: IWalletRepo = Depends(get_wallet_repo),  
    user: UserModel = Depends(get_authenticated_token_payload),
):
    try:
        add_transaction_usecase = AddTransaction(wallet_repo)
        output = await add_transaction_usecase.execute(wallet_id, transaction)
        return output.model_dump(mode="json")
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))