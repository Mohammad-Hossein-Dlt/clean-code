from enum import Enum

class UserType(str, Enum):
    admin = "admin"
    reqular = "reqular"
    
class PayoutStatus(str, Enum):
    pending = "pending"
    approved = "approved"
    paid = "paid"
    rejected = "rejected"
    
class PaymentMethod(str, Enum):
    paypal = "paypal"
    bank = "bank"
    crypto = "crypto"