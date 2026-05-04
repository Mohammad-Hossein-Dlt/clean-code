from src.repo.interface.Iwallet_repo import IWalletRepo
from src.domain.schemas.user.wallet_model import WalletModel
from src.infra.exceptions.exceptions import AppBaseException, OperationFailureException

class CreateWallet:
    
    def __init__(
        self,
        wallet_repo: IWalletRepo,
    ):
        
        self.wallet_repo = wallet_repo    
    
    async def execute(
        self,
        user_id: str,
    ) -> WalletModel:
        
        try:
            return await self.wallet_repo.create(
                WalletModel(
                    user_id=user_id,
                    available_balance=0,
                    pending_balance=0,
                    transactions=[],
                ),
            )
        except AppBaseException:
            raise
        except:
            raise OperationFailureException(500, "Internal server error")  