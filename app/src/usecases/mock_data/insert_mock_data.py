from app.src.domain.schemas.payout.payout_model import PayoutModel
from app.src.domain.schemas.user.wallet_model import WalletModel
from app.src.repo.interface.Imock_repo import IMockRepo
from app.src.domain.schemas.user.user_model import UserModel
from app.src.infra.exceptions.exceptions import OperationFailureException

class InsertMockData:
    
    def __init__(
        self,
        mock_repo: IMockRepo,
    ):
        
        self.mock_repo = mock_repo    
    
    async def execute(
        self,
        mock_users: list[UserModel],
        mock_wallets: list[WalletModel],
        mock_payouts: list[PayoutModel],
    ) -> dict:
        
        try:
            mock_users_id = await self.mock_repo.insert_many_users(mock_users)
            mock_wallets_id = await self.mock_repo.insert_many_wallets(mock_wallets)
            mock_payouts_id = await self.mock_repo.insert_many_payout(mock_payouts)
            
            return {
                "mock_users_id": mock_users_id,
                "mock_wallets_id": mock_wallets_id,
                "mock_payouts_id": mock_payouts_id,
            }
        except:
            raise OperationFailureException(500, "Internal server error")