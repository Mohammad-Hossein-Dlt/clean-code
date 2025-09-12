import unittest
from app.src.domain.schemas.user.user_model import UserModel
from app.src.domain.enums import UserType
from datetime import datetime, timedelta, timezone
from faker import Faker
import random

class UserModelTest:
    
    def test_validation(self, sample: dict):
        
        user = UserModel(**sample)
        user_dict = user.model_dump(by_alias=True, mode="json", exclude_unset=True)
                        
        return user_dict
        


class UserModelTestExample(unittest.TestCase):
    
    def setUp(self):

        datetime_format = "%Y-%m-%dT%H:%M:%SZ"
        now = datetime.now(timezone.utc)
        
        created = now.strftime(datetime_format)
        updated = (now + timedelta(days=15)).strftime(datetime_format)
        
        faker = Faker()
        
        self.sample = {
            "_id": "666f6f2d6261722d71757578",
            "name": faker.name(),
            "email": faker.email(),
            "username": faker.user_name(),
            "password": faker.password(),
            "user_type": random.choice([UserType.reqular.value, UserType.admin.value]),
            "created": created,
            "updated": updated,
        }
        
        self.test_model = UserModelTest()
        
        return super().setUp()
    
    def test_validation(self):
        self.assertDictEqual(self.test_model.test_validation(self.sample), self.sample)
        
