from abc import ABC, abstractmethod
from app.src.domain.schemas.user.user_model import UserModel
from app.src.domain.schemas.user.wallet_model import WalletModel, TransactionModel


class IUserRepo(ABC):
    
    @abstractmethod
    def insert_user(
        user: UserModel,
    ) -> UserModel | None:
    
        raise NotImplementedError
    
    @abstractmethod
    def delete_user(
        user_id: str,
    ) -> bool:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_user_by_id(
        user_id: str,
    ) ->  UserModel | None:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_user_by_username(
        username: str,
    ) -> UserModel | None:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_user_by_email(
        email: str,
    ) -> UserModel | None:
    
        raise NotImplementedError
        
    @abstractmethod
    def get_all_users() -> list[UserModel]:
        raise NotImplementedError
    
    @abstractmethod
    def insert_user_wallet(
        wallet: WalletModel,
    ) -> WalletModel | None:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_all_user_wallets(
        user_id: str,
    ) -> list[WalletModel]:
    
        raise NotImplementedError
    
    @abstractmethod
    def add_transaction(
        user_id: str,
        wallet_id: str,
        transaction: TransactionModel,
    ) -> WalletModel | None:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_balances(
        user_id: str,
    ) -> tuple[float, float]:
    
        raise NotImplementedError
    