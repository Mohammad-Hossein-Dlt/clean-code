import random
import unittest
from pydantic import BaseModel
from app.src.models.schemas.user.login_user_input import LoginUserInput
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


class LoginUserInputTestExample(unittest.TestCase):

    def setUp(self):
        
        faker = Faker()

        self.sample = {
            "username": faker.user_name(),
            "password": faker.password(),
        }
        
        self.test_model = BaseModelTest(LoginUserInput)

        return super().setUp()

    def test_validation(self):
        self.assertDictEqual(
            self.test_model.test_validation(self.sample),
            self.sample
        )
