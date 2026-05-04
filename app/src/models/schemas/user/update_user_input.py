from pydantic import BaseModel

class UpdateUserInput(BaseModel):
    name: str | None = None
    email: str | None = None