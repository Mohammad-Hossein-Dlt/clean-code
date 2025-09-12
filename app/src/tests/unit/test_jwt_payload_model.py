import unittest
from datetime import datetime, timedelta, timezone
from app.src.domain.schemas.auth.jwt_payload import JWTPayload

class JWTPayloadModelTest:
    
    def test_validation(self, sample: dict):
        
        payload = JWTPayload(**sample)
        payload_dict = payload.model_dump(mode="json")
                                                
        return payload_dict
        


class JWTPayloadModelTestExample(unittest.TestCase):
    
    def setUp(self):
        
        datetime_format = "%Y-%m-%dT%H:%M:%SZ"
        
        now = datetime.now(timezone.utc)
        
        exp = (now + timedelta(minutes=10)).strftime(datetime_format)
            
        
        self.sample = {
            "user_id": "650f9c2e5d9f4c1b8f3a12d7",
            "user_type": "reqular",
            "exp": exp,
        }
                                
        self.test_model = JWTPayloadModelTest()
        
        return super().setUp()
    
    def test_validation(self):
        self.assertDictEqual(self.test_model.test_validation(self.sample), self.sample)
        
