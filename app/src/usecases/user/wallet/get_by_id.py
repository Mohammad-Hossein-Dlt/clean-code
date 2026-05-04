from src.repo.interface.Iwallet_repo import IWalletRepo
from src.domain.schemas.user.wallet_model import WalletModel
from src.infra.exceptions.exceptions import AppBaseException, OperationFailureException

class GetWallet:
    
    def __init__(
        self,
        wallet_repo: IWalletRepo,
    ):
        
        self.wallet_repo = wallet_repo
    
    async def execute(
        self,
        wallet_id: str
    ) -> WalletModel:
        
        try:
            return await self.wallet_repo.get_by_id(wallet_id)
        except AppBaseException:
            raise
        except:
            raise OperationFailureException(500, "Internal server error")  