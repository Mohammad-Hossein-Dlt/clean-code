from datetime import datetime
from pydantic import BaseModel

class UserTransactionInput(BaseModel):
    amount: float
    date_available: datetime
