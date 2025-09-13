from pydantic import BaseModel, Field, model_validator
from beanie import PydanticObjectId
from bson.objectid import ObjectId
from app.src.domain.enums import UserType
from datetime import datetime, timezone


class UserModel(BaseModel):
    id: PydanticObjectId = Field(default_factory=ObjectId)
    name: str
    email: str
    username: str
    password: str
    user_type: UserType
    created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    @model_validator(mode="before")
    def map_id(cls, values: dict) -> dict:

        if "_id" in values:
            values["id"] = values.pop("_id")
        return values