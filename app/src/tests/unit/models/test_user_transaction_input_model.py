import unittest
from pydantic import BaseModel
from app.src.models.schemas.user.user_transaction_input import UserTransactionInput
from faker import Faker
from datetime import datetime, timedelta, timezone
import random

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

class UserTransactionInputTestExample(unittest.TestCase):

    def setUp(self):
        
        faker = Faker()
        
        datetime_format = "%Y-%m-%dT%H:%M:%SZ"
        now = datetime.now(timezone.utc)
        
        self.sample = {
            "amount": round(faker.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
            "date_available": (now + timedelta(days=random.randint(1, 30))).strftime(datetime_format),
        }
        
        self.test_model = BaseModelTest(UserTransactionInput)

        return super().setUp()

    def test_validation(self):
        self.assertDictEqual(
            self.test_model.test_validation(self.sample),
            self.sample
        )
