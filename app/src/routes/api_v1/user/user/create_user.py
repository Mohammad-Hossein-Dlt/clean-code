from ._router import router
from fastapi import Depends, HTTPException
from app.src.routes.http_response.responses import ResponseMessage
from app.src.models.schemas.user.create_user_input import CreateUserInput
from app.src.usecases.user.user.create_user import CreateUser
from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.routes.depends.user_repo_depend import get_user_repo
from app.src.infra.auth.jwt_handler import JWTHandler
from app.src.routes.depends.auth_depend import get_jwt_handler
from app.src.infra.exceptions.exceptions import AppBaseException

@router.post(
    "/create",
    status_code=201,
    responses={
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }
)
async def create_user(
    user_data: CreateUserInput = Depends(CreateUserInput),
    user_repo: IUserRepo = Depends(get_user_repo),
    jwt_handler: JWTHandler = Depends(get_jwt_handler),
):
    try:
        create_user_usecase = CreateUser(user_repo, jwt_handler)
        return await create_user_usecase.execute(user_data)
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))
