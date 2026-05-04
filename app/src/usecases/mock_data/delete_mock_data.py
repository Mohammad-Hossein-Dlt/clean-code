from src.repo.interface.Imock_repo import IMockRepo
from src.domain.schemas.user.user_model import UserModel
from src.models.schemas.operation.operation_output import OperationOutput
from src.infra.exceptions.exceptions import AppBaseException, OperationFailureException

class DeleteMockData:
    
    def __init__(
        self,
        mock_repo: IMockRepo,
    ):
        
        self.mock_repo = mock_repo    
    
    async def execute(
        self,
        mock_users: list[UserModel],
    ) -> bool:
        
        try:
            status = await self.mock_repo.delete_mock_data(mock_users)
            return OperationOutput(id=None, request="delete/mock-data", status=status)
        except AppBaseException:
            raise
        except:
            raise OperationFailureException(500, "Internal server error")  