from abc import ABC, abstractmethod
from app.src.models.filter.payout_filter import PayoutFilter
from app.src.domain.schemas.payout.payout_model import PayoutModel


class IPayoutRepo(ABC):
    
    def __init__(self, page_size: int):
        self.page_size = page_size  
    
    @abstractmethod
    def count_by_filter(payout_filter: PayoutFilter) -> int:
        raise NotImplementedError
    
    @abstractmethod
    def get_all_by_filter(payout_filter: PayoutFilter) -> list[PayoutModel]:
        raise NotImplementedError
    