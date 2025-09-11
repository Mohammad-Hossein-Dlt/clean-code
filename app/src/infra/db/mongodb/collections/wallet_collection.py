from beanie import Document
from app.src.domain.schemas.user.wallet_model import WalletModel

class WalletCollection(WalletModel, Document):
    class Settings:
        name = "Wallet"        
