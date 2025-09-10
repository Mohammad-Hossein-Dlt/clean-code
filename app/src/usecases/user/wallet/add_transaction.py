from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.domain.schemas.user.wallet_model import WalletModel, TransactionModel
from app.src.infra.exception.exceptions import OperationFailureException

class AddTransaction:
    
    def __init__(
        self,
        user_repo: IUserRepo,
    ):
        
        self.user_repo = user_repo    
    
    async def execute(
        self,
        user_id: str,
        transaction: TransactionModel,
    ) -> WalletModel:
        
        try:
            return await self.user_repo.add_transaction(user_id, TransactionModel.model_validate(transaction, from_attributes=True))
        except:
            raise OperationFailureException(500, "Internal server error")  