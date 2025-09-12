from pydantic import BaseModel
from datetime import datetime
from app.src.domain.enums import UserType

class JWTPayload(BaseModel):
    user_id: str
    user_type: UserType
    exp: datetime | None = None