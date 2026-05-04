from pydantic import BaseModel
from src.domain.enums import UserType

class CreateUserInput(BaseModel):
    name: str
    email: str
    username: str
    password: str
    user_type: UserType = UserType.reqular
