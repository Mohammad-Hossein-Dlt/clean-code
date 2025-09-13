import unittest
from pydantic import BaseModel
from app.src.models.filter.payout_filter import PayoutFilter
from app.src.domain.enums import UserType, PayoutStatus
from datetime import datetime, timedelta, timezone
import random
from faker import Faker

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

class PayoutFilterTestExample(unittest.TestCase):

    def setUp(self):
        
        faker = Faker()
        
        datetime_format = "%Y-%m-%dT%H:%M:%SZ"
        now = datetime.now(timezone.utc)

        self.sample = {
            "page": faker.random_int(min=1, max=10),
            "user_type": random.choice(
                [ user_type.value for user_type in UserType ],
            ),
            "statuses": [
                random.choice(
                    [ status.value for status in PayoutStatus ],
                ) for _ in range(2)
            ],
            "payment_start_date": (now - timedelta(days=30)).strftime(datetime_format),
            "payment_end_date": (now + timedelta(days=30)).strftime(datetime_format),
            "start_date": (now - timedelta(days=30)).strftime(datetime_format),
            "end_date": (now + timedelta(days=30)).strftime(datetime_format),
            "add_wallet": faker.boolean(),
        }

        self.test_model = BaseModelTest(PayoutFilter)

        return super().setUp()

    def test_validation(self):
        self.assertDictEqual(
            self.test_model.test_validation(self.sample),
            self.sample
        )
