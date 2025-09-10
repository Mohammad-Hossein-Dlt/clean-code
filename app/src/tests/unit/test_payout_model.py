from datetime import datetime, timedelta, timezone
import unittest
from app.src.domain.schemas.payout.payout_model import PayoutModel

class TestPayoutModel:
    
    def test_validation(self, sample: dict):
        
        wallet = PayoutModel(**sample)
        wallet_dict = wallet.model_dump(by_alias=True, mode="json", exclude_unset=True)
                                        
        return wallet_dict
        


class PayoutTestExample(unittest.TestCase):
    
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
                                
        self.test_model = TestPayoutModel()
        
        return super().setUp()
    
    def test_validation(self):
        self.assertDictEqual(self.test_model.test_validation(self.sample), self.sample)
        
