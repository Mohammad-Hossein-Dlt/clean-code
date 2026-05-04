from ._router import router
from fastapi import Depends, HTTPException
from src.routes.http_response.responses import ResponseMessage
from src.models.schemas.user.create_user_input import CreateUserInput
from src.repo.interface.Iuser_repo import IUserRepo
from src.routes.depends.repo_depend import get_user_repo
from src.usecases.user.user.create import CreateUser
from src.infra.exceptions.exceptions import AppBaseException

@router.post(
    "/",
    status_code=201,
    responses={
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }
)
async def create(
    entity: CreateUserInput = Depends(CreateUserInput),
    user_repo: IUserRepo = Depends(get_user_repo),
):
    try:
        create_user_usecase = CreateUser(user_repo)
        output = await create_user_usecase.execute(entity)
        return output.model_dump(mode="json")
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))
