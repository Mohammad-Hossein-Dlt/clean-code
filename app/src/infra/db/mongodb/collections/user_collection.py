from beanie import Document
from app.src.domain.schemas.user.user_model import UserModel

class UserCollection(UserModel, Document):
    class Settings:
        name = "User"
