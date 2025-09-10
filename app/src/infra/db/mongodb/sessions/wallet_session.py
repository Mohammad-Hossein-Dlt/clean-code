from beanie import Document
from app.src.domain.schemas.user.wallet_model import WalletModel

class WalletSession(WalletModel, Document):
    class Settings:
        name = "Wallet"        
