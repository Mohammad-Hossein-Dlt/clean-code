from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.domain.schemas.user.wallet_model import WalletModel
from app.src.infra.exceptions.exceptions import OperationFailureException

class CreateWallet:
    
    def __init__(
        self,
        user_repo: IUserRepo,
    ):
        
        self.user_repo = user_repo    
    
    async def execute(
        self,
        user_id: str,
    ) -> WalletModel:
        
        try:
            wallet: WalletModel = await self.user_repo.insert_user_wallet(WalletModel(user_id=user_id))
            return wallet.model_dump(mode="json")
        except:
            raise OperationFailureException(500, "Internal server error")  