import random
import unittest
from pydantic import BaseModel
from app.src.domain.enums import UserType
from app.src.models.schemas.user.create_user_input import CreateUserInput
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

class CreateUserInputTestExample(unittest.TestCase):

    def setUp(self):
        
        faker = Faker()

        self.sample = {
            "name": faker.name(),
            "email": faker.email(),
            "username": faker.user_name(),
            "password": faker.password(),
            "user_type": random.choice(
                [ user_type.value for user_type in UserType ],
            ),
        }
        
        self.test_model = BaseModelTest(CreateUserInput)

        return super().setUp()

    def test_validation(self):
        self.assertDictEqual(
            self.test_model.test_validation(self.sample),
            self.sample
        )
