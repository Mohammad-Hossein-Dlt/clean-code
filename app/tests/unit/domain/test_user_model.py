import unittest
from pydantic import BaseModel
from app.src.domain.schemas.user.user_model import UserModel
from app.src.domain.enums import UserType
from datetime import datetime, timedelta, timezone
from faker import Faker
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
        
class UserModelTestExample(unittest.TestCase):
    
    def setUp(self):
        
        faker = Faker()

        datetime_format = "%Y-%m-%dT%H:%M:%SZ"
        now = datetime.now(timezone.utc)
                
        self.sample = {
            "id":str(ObjectId()),
            "name": faker.name(),
            "email": faker.email(),
            "username": faker.user_name(),
            "password": faker.password(),
            "user_type": random.choice(
                [ user_type.value for user_type in UserType ],
            ),
            "created": (now - timedelta(days=15)).strftime(datetime_format),
            "updated": (now - timedelta(days=5)).strftime(datetime_format),
        }
        
        self.test_model = BaseModelTest(UserModel)
        
        return super().setUp()
    
    def test_validation(self):
        self.assertDictEqual(
            self.test_model.test_validation(self.sample),
            self.sample,
        )    
