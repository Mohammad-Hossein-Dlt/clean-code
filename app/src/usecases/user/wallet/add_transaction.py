from src.repo.interface.Iwallet_repo import IWalletRepo
from src.domain.schemas.user.wallet_model import WalletModel, TransactionModel
from src.infra.exceptions.exceptions import AppBaseException, OperationFailureException

class AddTransaction:
    
    def __init__(
        self,
        wallet_repo: IWalletRepo,
    ):
        
        self.wallet_repo = wallet_repo    
    
    async def execute(
        self,
        wallet_id: str,
        transaction: TransactionModel,
    ) -> WalletModel:
        
        try:
            transaction_model: TransactionModel = TransactionModel.model_validate(transaction, from_attributes=True)
            wallet: WalletModel = await self.wallet_repo.get_by_id(wallet_id)
            wallet.transactions.append(transaction_model)
            wallet.updated_at = transaction_model.created_at
            return await self.wallet_repo.update(wallet)
        except AppBaseException:
            raise
        except:
            raise OperationFailureException(500, "Internal server error")  