from pydantic import BaseModel, ConfigDict

class JwtParams(BaseModel):
    secret: str
    algorithm: str
    expiration: int

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
