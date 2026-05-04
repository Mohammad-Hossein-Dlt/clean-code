from src.repo.interface.Iuser_repo import IUserRepo
from src.repo.interface.Iwallet_repo import IWalletRepo
from src.domain.schemas.user.wallet_model import WalletModel
from src.infra.exceptions.exceptions import AppBaseException, OperationFailureException
from datetime import datetime, timezone

class GetBalances:
    
    def __init__(
        self,
        user_repo: IUserRepo,
        wallet_repo: IWalletRepo,
    ):
        
        self.user_repo = user_repo
        self.wallet_repo = wallet_repo
    
    async def execute(
        self,
        user_id: str,
    ) -> tuple[float, float]:
        
        try:
            wallets_list: list[WalletModel] = await self.wallet_repo.get_by_user_id(user_id)
            
            if not wallets_list:
                return 0, 0
            
            total_available_balance = 0
            total_pending_balance = 0
            for wallet in wallets_list:
                
                transactions_to_delete = []
                
                for trns in wallet.transactions:
                    if trns.date_available.astimezone(timezone.utc) <= datetime.now(timezone.utc):
                        wallet.available_balance += trns.amount
                        transactions_to_delete.append(str(trns.id))
                    else:
                        wallet.pending_balance += trns.amount
                            
                wallet.transactions = [trns for trns in wallet.transactions if str(trns.id) not in transactions_to_delete]            
                await self.wallet_repo.update(wallet)
                
                total_available_balance += wallet.available_balance
                total_pending_balance += wallet.pending_balance
            
            return total_available_balance, total_pending_balance
        except AppBaseException:
            raise
        except:
            raise OperationFailureException(500, "Internal server error")  