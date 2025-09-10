from app.src.repo.interface.Imock_repo import IMockRepo
from app.src.domain.schemas.user.user_model import UserModel
from app.src.infra.exception.exceptions import OperationFailureException

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
            return await self.mock_repo.delete_mock_data(mock_users)
        except:
            raise OperationFailureException(500, "Internal server error")