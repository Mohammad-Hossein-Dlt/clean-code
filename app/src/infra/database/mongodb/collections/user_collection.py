from src.domain.schemas.user.user_model import UserModel
from src.domain.enums import UserType
from pydantic import Field, model_validator
from beanie import Document, before_event, Update
from beanie import PydanticObjectId
from bson.objectid import ObjectId
from datetime import datetime, timezone

class UserCollection(UserModel, Document):
    
    id: PydanticObjectId = Field(default_factory=ObjectId)
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
        
    @model_validator(mode="before")
    def map_id(cls, values: dict) -> dict:

        if "_id" in values:
            values["id"] = values.pop("_id")
        return values
