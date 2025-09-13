import unittest
from pydantic import BaseModel
from app.src.models.schemas.user.login_user_output import LoginUserOutput
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

class LoginUserOutputTestExample(unittest.TestCase):

    def setUp(self):
        
        faker = Faker()

        self.sample = {
            "access_token": faker.sentence()
        }
        
        self.test_model = BaseModelTest(LoginUserOutput)

        return super().setUp()

    def test_validation(self):
        self.assertDictEqual(
            self.test_model.test_validation(self.sample),
            self.sample
        )
