from src.repo.interface.Iuser_repo import IUserRepo
from src.repo.interface.Iwallet_repo import IWalletRepo
from src.repo.interface.Ipayout_repo import IPayoutRepo
from src.domain.schemas.user.user_model import UserModel
from src.domain.schemas.user.wallet_model import WalletModel
from src.domain.schemas.payout.payout_model import PayoutModel
from src.models.schemas.operation.operation_output import OperationOutput
from src.infra.exceptions.exceptions import AppBaseException, OperationFailureException

class InsertMockData:
    
    def __init__(
        self,
        user_repo: IUserRepo,
        wallet_repo: IWalletRepo,
        payout_repo: IPayoutRepo,
    ):
        
        self.user_repo = user_repo
        self.wallet_repo = wallet_repo
        self.payout_repo = payout_repo
    
    async def execute(
        self,
        mock_users: list[UserModel],
        mock_wallets: list[WalletModel],
        mock_payouts: list[PayoutModel],
    ) -> dict:
        
        try:
            
            try:
                for user in mock_users:
                    await self.user_repo.create_mock(user)            
                
                for wallet in mock_wallets:
                    await self.wallet_repo.create_mock(wallet)            
                
                for payout in mock_payouts:
                    await self.payout_repo.create_mock(payout)
            except:
                ...
                                    
            return OperationOutput(id=None, request="create/mock-data", status=True)
        except AppBaseException:
            raise
        except:
            raise OperationFailureException(500, "Internal server error")  