from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.domain.schemas.user.wallet_model import WalletModel
from app.src.infra.exceptions.exceptions import OperationFailureException

class GetAllUserWallets:
    
    def __init__(
        self,
        user_repo: IUserRepo,
    ):
        
        self.user_repo = user_repo    
    
    async def execute(
        self,
        user_id: str,
    ) -> list[WalletModel]:
        
        try:
            all_wallets: list[WalletModel] = await self.user_repo.get_all_user_wallets(user_id)
            return [ wallet.model_dump(mode="json") for wallet in all_wallets ]
        except:
            raise OperationFailureException(500, "Internal server error")