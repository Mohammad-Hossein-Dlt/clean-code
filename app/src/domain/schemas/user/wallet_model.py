from src.infra.utils.custom_base_model import CustomBaseModel
from pydantic import Field, ConfigDict, model_validator
from beanie import PydanticObjectId
from datetime import datetime, timezone
from typing import Self

class TransactionModel(CustomBaseModel):
    
    amount: float
    date_available: datetime
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    model_config = ConfigDict(
        extra='allow',
    )

    @model_validator(mode='after')
    def validate_values(
        self
    ) -> Self:
        
        if "updated_at" not in self.model_fields_set:
            self.updated_at = self.created_at
        
        return self

class WalletModel(CustomBaseModel):

    id: PydanticObjectId | None = None
    user_id: PydanticObjectId | None = None
    available_balance: float | None = None
    pending_balance: float | None = None
    transactions: list[TransactionModel] | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    model_config = ConfigDict(
        extra='allow',
    )

    @model_validator(mode='after')
    def validate_values(
        self
    ) -> Self:
        
        if "updated_at" not in self.model_fields_set:
            self.updated_at = self.created_at
        
        return self