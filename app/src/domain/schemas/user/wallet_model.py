from beanie import PydanticObjectId
from datetime import datetime, timezone
from pydantic import BaseModel, Field
from bson.objectid import ObjectId

class TransactionModel(BaseModel):
    id: PydanticObjectId = Field(default_factory=ObjectId, alias="_id")
    amount: float
    date_available: datetime
    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class WalletModel(BaseModel):
    id: PydanticObjectId = Field(default_factory=ObjectId, alias="_id")
    user_id: PydanticObjectId
    available_balance: float = 0
    pending_balance: float = 0
    transactions: list[TransactionModel] = []
    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))   
