from ._router import router
from fastapi import Depends, HTTPException
from app.src.routes.http_response.responses import ResponseMessage
from app.src.domain.schemas.auth.jwt_payload import JWTPayload
from app.src.models.schemas.user.user_transaction_input import UserTransactionInput
from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.routes.depends.auth_depend import get_authenticated_token_payload
from app.src.routes.depends.user_repo_depend import get_user_repo
from app.src.usecases.user.wallet.add_transaction import AddTransaction 
from app.src.infra.exceptions.exceptions import AppBaseException

@router.put(
    "/transaction/add",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_401_UNAUTHORIZED("Authentication failed"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }
)
async def add_transaction(
    wallet_id: str,
    transaction: UserTransactionInput,
    user: JWTPayload = Depends(get_authenticated_token_payload),
    user_repo: IUserRepo = Depends(get_user_repo),
):
    try:
        add_transaction_usecase = AddTransaction(user_repo)
        return await add_transaction_usecase.execute(user.user_id, wallet_id, transaction)
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))