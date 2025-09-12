from abc import ABC, abstractmethod
from app.src.domain.schemas.user.user_model import UserModel
from app.src.domain.schemas.user.wallet_model import WalletModel
from app.src.domain.schemas.payout.payout_model import PayoutModel


class IMockRepo(ABC):
    
    @abstractmethod
    def insert_many_users(
        users: list[UserModel],
    ) -> bool:
    
        raise NotImplementedError
    
    @abstractmethod
    def insert_many_wallets(
        wallets: list[WalletModel],
    ) -> bool:
    
        raise NotImplementedError    
        
    @abstractmethod
    def insert_many_payout(
        payouts: list[PayoutModel],
    ) -> bool:
    
        raise NotImplementedError    
    
            
    @abstractmethod
    def delete_mock_data(
        users: list[UserModel],
    ) -> bool:
    
        raise NotImplementedError    
    
    
