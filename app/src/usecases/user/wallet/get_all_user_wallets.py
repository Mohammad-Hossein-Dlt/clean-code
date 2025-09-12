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
            return await self.user_repo.get_all_user_wallets(user_id)
        except:
            raise OperationFailureException(500, "Internal server error")