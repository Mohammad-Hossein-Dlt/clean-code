from beanie import PydanticObjectId
from datetime import datetime, timezone
from pydantic import BaseModel, Field, model_validator
from bson.objectid import ObjectId

class TransactionModel(BaseModel):
    id: PydanticObjectId = Field(default_factory=ObjectId)
    amount: float
    date_available: datetime
    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    @model_validator(mode="before")
    def map_id(cls, values: dict) -> dict:

        if "_id" in values:
            values["id"] = values.pop("_id")
        return values


class WalletModel(BaseModel):
    id: PydanticObjectId = Field(default_factory=ObjectId)
    user_id: PydanticObjectId
    available_balance: float = 0
    pending_balance: float = 0
    transactions: list[TransactionModel] = []
    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))   
    
    @model_validator(mode="before")
    def map_id(cls, values: dict) -> dict:

        if "_id" in values:
            values["id"] = values.pop("_id")
        return values
