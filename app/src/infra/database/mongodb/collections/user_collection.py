from src.domain.schemas.user.user_model import UserModel
from src.domain.enums import UserType
from beanie import Document, before_event, Update
from beanie import PydanticObjectId
from datetime import datetime, timezone

class UserCollection(UserModel, Document):
    
    id: PydanticObjectId = None
    name: str
    email: str
    username: str
    password: str
    user_type: UserType
    
    class Settings:
        name = "User"

    @before_event(Update)
    def set_updated_at(self):
        self.updated_at = datetime.now(timezone.utc)