from src.domain.schemas.payout.payout_model import PayoutModel
from src.models.filter.payout_sriteria import PayoutCriteria
from src.domain.enums import UserType, PayoutStatus, PaymentMethod
from pydantic import Field, model_validator
from beanie import Document, before_event, Update
from beanie import PydanticObjectId
from bson.objectid import ObjectId
from datetime import datetime, timezone

class PayoutCollection(PayoutModel, Document):

    id: PydanticObjectId = Field(default_factory=ObjectId)
    affiliate_tracking_id: PydanticObjectId
    user_id: PydanticObjectId
    user_type: UserType
    amount: float
    status: PayoutStatus
    payment_method: PaymentMethod
    payment_date: datetime

    class Settings:
        name = "Payout"
        
    @before_event(Update)
    def set_updated_at(self):
        self.updated_at = datetime.now(timezone.utc)
        
    @model_validator(mode="before")
    def map_id(cls, values: dict) -> dict:

        if "_id" in values:
            values["id"] = values.pop("_id")
        return values


    @classmethod
    def create_query_by_criteria(
        cls,
        criteria: PayoutCriteria,
    ):
        
        query = {}

        if criteria.start_date:
            query[str(cls.created)] = {"$gte": criteria.start_date}

        if criteria.end_date:
            query.setdefault(str(cls.created), {})
            query[str(cls.created)]["$lte"] = criteria.end_date

        if criteria.payment_start_date:
            query[str(cls.payment_date)] = {"$gte": criteria.payment_start_date}

        if criteria.payment_end_date:
            query.setdefault(str(cls.payment_date), {})
            query[str(cls.payment_date)]["$lte"] = criteria.payment_end_date

        if criteria.user_type:
            query[str(cls.user_type)] = criteria.user_type.value

        if criteria.status:
            query[str(cls.status)] = {"$in": criteria.status}
            
        if criteria.payment_method:
            query[str(cls.payment_method)] = {"$in": criteria.payment_method}
                    
        return query