from beanie import PydanticObjectId
from datetime import datetime, timezone
from pydantic import BaseModel, ConfigDict, Field, model_validator
from bson.objectid import ObjectId
from app.src.domain.enums import UserType, PayoutStatus, PaymentMethod

def snake_to_camel(snake_str: str):
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])

class PayoutModel(BaseModel):
    id: PydanticObjectId = Field(default_factory=ObjectId)
    affiliate_tracking_id: PydanticObjectId
    user_id: PydanticObjectId
    user_type: UserType
    amount: float
    status: PayoutStatus
    payment_method: PaymentMethod
    payment_date: datetime
    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    model_config = ConfigDict(
        alias_generator= snake_to_camel,
        populate_by_name=True,
        extra='allow',
        json_encoders={
            ObjectId: str,
            PydanticObjectId: str
        }
    )
    
    @model_validator(mode="before")
    def map_id(cls, values: dict) -> dict:

        if "_id" in values:
            values["id"] = values.pop("_id")
        return values