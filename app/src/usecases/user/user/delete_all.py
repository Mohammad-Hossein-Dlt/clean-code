from src.repo.interface.Iuser_repo import IUserRepo
from src.models.schemas.operation.operation_output import OperationOutput
from src.infra.exceptions.exceptions import AppBaseException, OperationFailureException

class DeleteUsers:
    
    def __init__(
        self,
        user_repo: IUserRepo,
    ):
        
        self.user_repo = user_repo    
    
    async def execute(
        self,
    ) -> OperationOutput:
        
        try:
            status = await self.user_repo.delete_all()
            return OperationOutput(id=None, request="delete/all-users", status=status)
        except AppBaseException:
            raise
        except:
            raise OperationFailureException(500, "Internal server error")  