from app.src.routes.api_v1.mock_data._router import router
from fastapi import HTTPException, Depends
from app.src.routes.http_response.responses import ResponseMessage
from app.src.routes.depends.mock_repo_depend import get_mock_repo
from app.src.routes.depends.auth_depend import chech_admin_type
from app.src.domain.schemas.auth.jwt_payload import JWTPayload
from app.src.repo.interface.Ipayout_repo import IPayoutRepo
from app.src.domain.mock_data.mock_data import mock_users
from app.src.usecases.mock_data.delete_mock_data import DeleteMockData
from app.src.infra.exceptions.exceptions import AppBaseException


@router.delete(
    "/delete",
    status_code=200,
    responses={
        **ResponseMessage.HTTP_401_UNAUTHORIZED("Authentication failed"),
        **ResponseMessage.HTTP_403_FORBIDDEN("Access denied"),
        **ResponseMessage.HTTP_500_INTERNAL_SERVER_ERROR("Internal server error"),
    }
)
async def delete_mock_payouts(
    mock_repo: IPayoutRepo = Depends(get_mock_repo),
    admin: JWTPayload = Depends(chech_admin_type),
):
    try:
        delete_mock_data_usecase = DeleteMockData(mock_repo)
        return await delete_mock_data_usecase.execute(mock_users)
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=str(ex))
