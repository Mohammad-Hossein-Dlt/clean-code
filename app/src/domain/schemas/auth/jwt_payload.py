from pydantic import BaseModel
from src.domain.enums import UserType
from datetime import datetime

class JWTPayload(BaseModel):
    user_id: str
    user_type: UserType
    exp: datetime | None = None