from .base_filter_criteria import BaseFilterCriteria
from src.domain.enums import UserType, PayoutStatus, PaymentMethod
from datetime import datetime

class PayoutFilterInput(BaseFilterCriteria):
    user_type: UserType = None
    status: list[PayoutStatus] = None
    payment_method: list[PaymentMethod] = None
    payment_start_date: datetime = None
    payment_end_date: datetime = None
    start_date: datetime = None
    end_date: datetime = None
    add_wallet: bool = False
    
    
