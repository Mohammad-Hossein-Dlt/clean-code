from ._router import router
from fastapi import HTTPException, Depends
from src.routes.http_response.responses import ResponseMessage
from src.repo.interface.Ipayout_repo import IPayoutRepo
from src.routes.depends.repo_depend import get_mock_repo
from src.domain.schemas.user.user_model import UserModel
from src.routes.depends.auth_depend import check_admin_access
from src.usecases.mock_data.delete_mock_data import DeleteMockData
from src.domain.mock_data.mock_data import mock_users
from src.infra.exceptions.exceptions import AppBaseException


@router.delete(
    "/",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_401_UNAUTHORIZED("Authentication failed"),
        **ResponseMessage.HTTP_403_FORBIDDEN("Access denied"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }
)
async def delete_mock_payouts(
    mock_repo: IPayoutRepo = Depends(get_mock_repo),
    admin: UserModel = Depends(check_admin_access),
):
    try:
        delete_mock_data_usecase = DeleteMockData(mock_repo)
        output = await delete_mock_data_usecase.execute(mock_users)
        return output.model_dump(mode="json")
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))
