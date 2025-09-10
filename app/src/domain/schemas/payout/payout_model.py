from beanie import PydanticObjectId
from datetime import datetime, timezone
from pydantic import BaseModel, ConfigDict, Field
from bson.objectid import ObjectId
from app.src.domain.enums import UserType, PayoutStatus, PaymentMethod


def snake_to_camel(snake_str: str):
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])

class PayoutModel(BaseModel):
    id: PydanticObjectId = Field(default_factory=ObjectId, alias="_id")
    user_id: PydanticObjectId
    user_type: UserType = UserType.reqular
    amount: float
    status: PayoutStatus = PayoutStatus.pending
    payment_method: PaymentMethod = PaymentMethod.bank
    payment_date: datetime
    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    model_config = ConfigDict(
        alias_generator= snake_to_camel,
        populate_by_name=True,
        extra='allow',
    )
