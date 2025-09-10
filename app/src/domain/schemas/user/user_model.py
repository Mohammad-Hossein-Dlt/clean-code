from pydantic import BaseModel, Field
from beanie import PydanticObjectId
from bson.objectid import ObjectId
from app.src.domain.enums import UserType
from datetime import datetime, timezone


class UserModel(BaseModel):
    id: PydanticObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str
    email: str
    username: str
    password: str
    user_type: UserType = UserType.reqular
    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))