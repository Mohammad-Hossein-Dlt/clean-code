import unittest
from pydantic import BaseModel
from app.src.domain.enums import PaymentMethod, UserType, PayoutStatus
from app.src.models.schemas.payout.payout_paginate import PayoutPaginate
from datetime import datetime, timedelta, timezone
import random
from bson.objectid import ObjectId

class BaseModelTest:

    def __init__(
        self,
        model_class: BaseModel,
    ):
        
        self.model_class: BaseModel = model_class
    
    def test_validation(
        self,
        sample: dict,
    ):
        
        model_instance: BaseModel = self.model_class(**sample)
        model_dict = model_instance.model_dump(by_alias=True, mode="json")
                                                                
        return model_dict

class PayoutPaginateTestExample(unittest.TestCase):
    
    def setUp(self):
        
        datetime_format = "%Y-%m-%dT%H:%M:%SZ"
        now = datetime.now(timezone.utc)

        payout_samples = []
        payout_samples_with_alias = []
        for _ in range(4):
            sample = {
                "id": str(ObjectId()),
                "affiliate_tracking_id": str(ObjectId()),
                "user_id": str(ObjectId()),
                "user_type": random.choice(
                    [ user_type.value for user_type in UserType ],
                ),
                "amount": round(random.uniform(50, 5000), 2),
                "status": random.choice(
                    [ status.value for status in PayoutStatus ],
                ),
                "payment_method": random.choice(
                    [ method.value for method in PaymentMethod ],
                ),
                "payment_date": (now + timedelta(days=random.randint(1, 30))).strftime(datetime_format),
                "created": (now - timedelta(days=random.randint(1, 30))).strftime(datetime_format),
            }
                        
            sample_with_alias = {
                "id": sample["id"],
                "affiliateTrackingId": sample["affiliate_tracking_id"],
                "userId": sample["user_id"],
                "userType": sample["user_type"],
                "amount": sample["amount"],
                "status": sample["status"],
                "paymentMethod": sample["payment_method"],
                "paymentDate": sample["payment_date"],
                "created": sample["created"],
            }
            
            payout_samples.append(sample)
            payout_samples_with_alias.append(sample_with_alias)

        self.sample = {
            "page": 1,
            "pageSize": 10,
            "totalPages": 5,
            "totalDocs": 45,
            "results": payout_samples
        }
        
        self.sample_with_alias = {
            "page": 1,
            "pageSize": 10,
            "totalPages": 5,
            "totalDocs": 45,
            "results": payout_samples_with_alias
        }
                
        self.test_model = BaseModelTest(PayoutPaginate)
        
        self.maxDiff = None
        return super().setUp()
        
    def test_validation(self):
        self.assertDictEqual(
            self.test_model.test_validation(self.sample),
            self.sample_with_alias
        )
