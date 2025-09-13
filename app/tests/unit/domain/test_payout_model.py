import unittest
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from app.src.domain.enums import UserType, PayoutStatus, PaymentMethod
from app.src.domain.schemas.payout.payout_model import PayoutModel
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
        
class PayoutModelTestExample(unittest.TestCase):
    
    def setUp(self):
        
        datetime_format = "%Y-%m-%dT%H:%M:%SZ"
        now = datetime.now(timezone.utc)
        
        self.sample = {
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
                
        self.sample_with_alias = {
            "id": self.sample["id"],
            "affiliateTrackingId": self.sample["affiliate_tracking_id"],
            "userId": self.sample["user_id"],
            "userType": self.sample["user_type"],
            "amount": self.sample["amount"],
            "status": self.sample["status"],
            "paymentMethod": self.sample["payment_method"],
            "paymentDate": self.sample["payment_date"],
            "created": self.sample["created"],
        }
            
        self.test_model = BaseModelTest(PayoutModel)
        
        return super().setUp()
    
    def test_validation(self):
        self.assertDictEqual(
            self.test_model.test_validation(self.sample),
            self.sample_with_alias,
        )
