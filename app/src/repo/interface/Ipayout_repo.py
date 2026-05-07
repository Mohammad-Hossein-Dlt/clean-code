from abc import ABC, abstractmethod
from src.domain.schemas.payout.payout_model import PayoutModel
from src.models.filter.payout_filter_input import PayoutFilterInput

class IPayoutRepo(ABC):
    
    @abstractmethod
    def create_mock(
        user: PayoutModel,
    ) -> PayoutModel:
    
        raise NotImplementedError
    
    @abstractmethod
    def create(
        user: PayoutModel,
    ) -> PayoutModel:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(
        payout_id: str,
    ) -> PayoutModel:
    
        raise NotImplementedError

    @abstractmethod
    def update(
        payout: PayoutModel,
    ) -> PayoutModel:
    
        raise NotImplementedError    

    @abstractmethod
    def delete_by_id(
        payout_id: str,
    ) -> bool:
    
        raise NotImplementedError

    @abstractmethod
    def get_by_user_id(
        user_id: str,
        criteria: PayoutFilterInput | None = None, 
    ) -> list[PayoutModel]:
    
        raise NotImplementedError
    
    @abstractmethod
    def delete_by_user_id(
        user_id: str,
    ) -> bool:
    
        raise NotImplementedError
    @abstractmethod
    
    @abstractmethod
    def count_by_criteria(
        criteria: PayoutFilterInput,
    ) -> int:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_by_criteria(
        criteria: PayoutFilterInput,
    ) -> list[PayoutModel]:
    
        raise NotImplementedError
    
    def delete_all() -> bool:
    
        raise NotImplementedError