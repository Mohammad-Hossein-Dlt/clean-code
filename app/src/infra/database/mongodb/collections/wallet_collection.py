from src.domain.schemas.user.wallet_model import WalletModel, TransactionModel
from pydantic import Field, model_validator
from beanie import Document, before_event, Update
from beanie import PydanticObjectId
from bson.objectid import ObjectId
from datetime import datetime, timezone

class WalletCollection(WalletModel, Document):
    
    id: PydanticObjectId = Field(default_factory=ObjectId)
    user_id: PydanticObjectId
    available_balance: float = 0
    pending_balance: float = 0
    transactions: list[TransactionModel] = []
    
    class Settings:
        name = "Wallet"        

    @before_event(Update)
    def set_updated_at(self):
        self.updated_at = datetime.now(timezone.utc)
        
    @model_validator(mode="before")
    def map_id(cls, values: dict) -> dict:

        if "_id" in values:
            values["id"] = values.pop("_id")
        return values
