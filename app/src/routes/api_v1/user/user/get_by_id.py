from ._router import router 
from fastapi import Depends, HTTPException
from src.routes.http_response.responses import ResponseMessage
from src.domain.schemas.user.user_model import UserModel
from src.repo.interface.Iuser_repo import IUserRepo
from src.routes.depends.auth_depend import get_authenticated_token_payload
from src.routes.depends.repo_depend import get_user_repo
from src.usecases.user.user.get_by_id import GetUser
from src.infra.exceptions.exceptions import AppBaseException

@router.get(
    "/by-id",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_401_UNAUTHORIZED("Authentication failed"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }
)
async def get_by_id(
    user_repo: IUserRepo = Depends(get_user_repo),
    user: UserModel = Depends(get_authenticated_token_payload)
):
    try:
        get_user_usecase = GetUser(user_repo)
        output = await get_user_usecase.execute(user.user_id)
        return output.model_dump(mode="json")
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))
