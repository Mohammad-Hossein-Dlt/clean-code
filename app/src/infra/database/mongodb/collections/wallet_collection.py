from src.domain.schemas.user.wallet_model import WalletModel, TransactionModel
from beanie import Document, before_event, Update
from beanie import PydanticObjectId
from datetime import datetime, timezone

class WalletCollection(WalletModel, Document):
    
    id: PydanticObjectId = None
    user_id: PydanticObjectId
    available_balance: float = 0
    pending_balance: float = 0
    transactions: list[TransactionModel] = []
    
    class Settings:
        name = "Wallet"        

    @before_event(Update)
    def set_updated_at(self):
        self.updated_at = datetime.now(timezone.utc)