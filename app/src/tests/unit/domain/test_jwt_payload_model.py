import random
import unittest
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from app.src.domain.enums import UserType
from app.src.domain.schemas.auth.jwt_payload import JWTPayload
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
        


class JWTPayloadModelTestExample(unittest.TestCase):
    
    def setUp(self):
        
        datetime_format = "%Y-%m-%dT%H:%M:%SZ"
        now = datetime.now(timezone.utc)
            
        self.sample = {
            "user_id": str(ObjectId),
            "user_type": random.choice(
                [ user_type.value for user_type in UserType ],
            ),
            "exp": (now + timedelta(minutes=10)).strftime(datetime_format),
        }
                                
        self.test_model = BaseModelTest(JWTPayload)
        
        return super().setUp()
    
    def test_validation(self):
        self.assertDictEqual(
            self.test_model.test_validation(self.sample),
            self.sample,
        )
        
