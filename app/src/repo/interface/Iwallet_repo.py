from abc import ABC, abstractmethod
from src.domain.schemas.user.wallet_model import WalletModel
from src.models.filter.base_filter_criteria import BaseFilterCriteria

class IWalletRepo(ABC):
    
    @abstractmethod
    def create_mock(
        wallet: WalletModel,
    ) -> WalletModel:
    
        raise NotImplementedError
    
    @abstractmethod
    def create(
        wallet: WalletModel,
    ) -> WalletModel:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(
        wallet_id: str,
    ) -> WalletModel:
    
        raise NotImplementedError
    
    @abstractmethod
    def update(
        wallet: WalletModel,
    ) -> WalletModel:
    
        raise NotImplementedError
    
    @abstractmethod
    def delete_by_id(
        wallet_id: str,
    ) -> bool:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_by_user_id(
        user_id: str,
        criteria: BaseFilterCriteria | None = None, 
    ) -> list[WalletModel]:
    
        raise NotImplementedError
    
    @abstractmethod
    def delete_by_user_id(
        user_id: str,
    ) -> bool:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_all(
        criteria: BaseFilterCriteria | None = None, 
    ) -> list[WalletModel]:
    
        raise NotImplementedError
    
    @abstractmethod
    def delete_all() -> bool:
    
        raise NotImplementedError