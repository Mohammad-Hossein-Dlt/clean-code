import unittest
from pydantic import BaseModel
from app.src.domain.schemas.user.wallet_model import WalletModel
from datetime import datetime, timedelta, timezone
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
        


class WalletModelTestExample(unittest.TestCase):
    
    def setUp(self):
        
        datetime_format = "%Y-%m-%dT%H:%M:%SZ"
        now = datetime.now(timezone.utc)
        
        self.sample = {
            "_id":str(ObjectId()),
            "user_id":str(ObjectId()),
            "available_balance": 150.75,
            "pending_balance": 20.00,
            "transactions": [
                {
                    "_id":str(ObjectId()),
                    "amount": 100.50,
                    "date_available": (now + timedelta(days=10)).strftime(datetime_format),
                    "created": (now - timedelta(days=5)).strftime(datetime_format),
                },
                {
                    "_id":str(ObjectId()),
                    "amount": 70.25,
                    "date_available": (now + timedelta(days=10)).strftime(datetime_format),
                    "created": (now - timedelta(days=5)).strftime(datetime_format),
                },
            ],
            "created": (now - timedelta(days=15)).strftime(datetime_format),
            "updated": (now - timedelta(days=5)).strftime(datetime_format),
        }
                        
        self.test_model = BaseModelTest(WalletModel)
        
        return super().setUp()
    
    def test_validation(self):
        self.assertDictEqual(
            self.test_model.test_validation(self.sample),
            self.sample,
        ) 