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
            "_id": str(ObjectId()),
            "affiliate_tracking_id": str(ObjectId()),
            "userId": str(ObjectId()),
            "userType": random.choice(
                [ user_type.value for user_type in UserType ],
            ),
            "amount": 250.0,
            "status": random.choice(
                [ status.value for status in PayoutStatus ],
            ),
            "paymentMethod": random.choice(
                [ method.value for method in PaymentMethod ],
            ),
            "paymentDate": (now + timedelta(days=5)).strftime(datetime_format),
            "created": (now - timedelta(days=5)).strftime(datetime_format),
        }
                                
        self.test_model = BaseModelTest(PayoutModel)
        
        return super().setUp()
    
    def test_validation(self):
        self.assertDictEqual(
            self.test_model.test_validation(self.sample),
            self.sample,
        )
