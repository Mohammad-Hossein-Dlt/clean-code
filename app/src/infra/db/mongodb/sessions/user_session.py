from beanie import Document
from app.src.domain.schemas.user.user_model import UserModel

class UserSession(UserModel, Document):
    class Settings:
        name = "User"
