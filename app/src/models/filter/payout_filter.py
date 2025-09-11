from pydantic import BaseModel
from app.src.domain.enums import UserType, PayoutStatus
from datetime import datetime

class PayoutFilter(BaseModel):
    page: int = None
    user_type: UserType = None
    statuses: list[PayoutStatus] = None
    payment_start_date: datetime = None
    payment_end_date: datetime = None
    start_date: datetime = None
    end_date: datetime = None
    add_wallet: bool = False
    
    
