import unittest
from datetime import datetime, timedelta, timezone
from app.src.domain.schemas.payout.payout_model import PayoutModel

class PayoutModelTest:
    
    def test_validation(self, sample: dict):
        
        payout = PayoutModel(**sample)
        payout_dict = payout.model_dump(by_alias=True, mode="json", exclude_unset=True)
                                        
        return payout_dict
        


class PayoutModelTestExample(unittest.TestCase):
    
    def setUp(self):
        
        datetime_format = "%Y-%m-%dT%H:%M:%SZ"
        
        now = datetime.now(timezone.utc)
        
        created = now.strftime(datetime_format)
        paymentDate = (now + timedelta(days=15)).strftime(datetime_format)
            
        
        self.sample = {
            "_id": "650f9c2e5d9f4c1b8f3a12d7",
            "userId": "650f9c2e5d9f4c1b8f3a12d7",
            "userType": "reqular",
            "amount": 250.0,
            "status": "pending",       
            "paymentMethod": "bank",
            "paymentDate": paymentDate,
            "created": created,
        }
                                
        self.test_model = PayoutModelTest()
        
        return super().setUp()
    
    def test_validation(self):
        self.assertDictEqual(self.test_model.test_validation(self.sample), self.sample)
        
