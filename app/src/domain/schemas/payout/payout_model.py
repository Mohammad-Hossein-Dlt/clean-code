from src.infra.utils.custom_base_model import CustomBaseModel
from src.domain.enums import UserType, PayoutStatus, PaymentMethod
from pydantic import ConfigDict, Field, model_validator
from beanie import PydanticObjectId
from bson.objectid import ObjectId
from datetime import datetime, timezone
from typing import Self

def snake_to_camel(snake_str: str):
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])

class PayoutModel(CustomBaseModel):
    id: PydanticObjectId = Field(default_factory=ObjectId)
    affiliate_tracking_id: PydanticObjectId | None = None
    user_id: PydanticObjectId | None = None
    user_type: UserType | None = None
    amount: float | None = None
    status: PayoutStatus | None = None
    payment_method: PaymentMethod | None = None
    payment_date: datetime | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    model_config = ConfigDict(
        alias_generator= snake_to_camel,
        populate_by_name=True,
        extra='allow',
        json_encoders={
            ObjectId: str,
            PydanticObjectId: str
        }
    )

    @model_validator(mode='after')
    def validate_values(
        self
    ) -> Self:
        
        if "updated_at" not in self.model_fields_set:
            self.updated_at = self.created_at
        
        return self