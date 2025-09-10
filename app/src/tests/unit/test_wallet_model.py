from datetime import datetime, timedelta, timezone
import unittest
from app.src.domain.schemas.user.wallet_model import WalletModel

class TestWalletModel:
    
    def test_validation(self, sample: dict):
        
        wallet = WalletModel(**sample)
        wallet_dict = wallet.model_dump(by_alias=True, mode="json", exclude_unset=True)
                                        
        return wallet_dict
        


class WalletTestExample(unittest.TestCase):
    
    def setUp(self):
        
        datetime_format = "%Y-%m-%dT%H:%M:%SZ"
        
        now = datetime.now(timezone.utc)
        
        created = now.strftime(datetime_format)
        updated = (now + timedelta(days=15)).strftime(datetime_format)
        date_available = (now + timedelta(days=15)).strftime(datetime_format)
            
        
        self.sample = {
            "_id": "650f9c2e5d9f4c1b8f3a12d7",
            "user_id": "650f9c3a5d9f4c1b8f3a12d8",
            "available_balance": 150.75,
            "pending_balance": 20.00,
            "transactions": [
                {
                    "_id": "650f9c4b5d9f4c1b8f3a12d9",
                    "amount": 100.50,
                    "date_available": date_available,
                    "created": created,
                },
                {
                    "_id": "650f9c5d5d9f4c1b8f3a12da",
                    "amount": 70.25,
                    "date_available": date_available,
                    "created": created,
                },
            ],
            "created": created,
            "updated": updated,
        }
                        
        self.test_model = TestWalletModel()
        
        return super().setUp()
    
    def test_validation(self):
        self.assertDictEqual(self.test_model.test_validation(self.sample), self.sample)
        