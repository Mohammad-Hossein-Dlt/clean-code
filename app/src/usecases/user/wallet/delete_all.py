from src.repo.interface.Iwallet_repo import IWalletRepo
from src.models.schemas.operation.operation_output import OperationOutput
from src.infra.exceptions.exceptions import AppBaseException, OperationFailureException

class DeleteWallets:
    
    def __init__(
        self,
        wallet_repo: IWalletRepo,
    ):
        
        self.wallet_repo = wallet_repo    
    
    async def execute(
        self,
    ) -> OperationOutput:
        
        try:
            status = await self.wallet_repo.delete_all()
            return OperationOutput(id=None, request="delete/all-wallets", status=status)
        except AppBaseException:
            raise
        except:
            raise OperationFailureException(500, "Internal server error")  