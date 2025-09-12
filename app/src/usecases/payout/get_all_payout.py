from app.src.models.filter.payout_filter import PayoutFilter
from app.src.models.schemas.payout.payout_paginate import PayoutPaginate
from app.src.repo.interface.Ipayout_repo import IPayoutRepo
from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.domain.schemas.payout.payout_model import PayoutModel
from app.src.infra.exceptions.exceptions import OperationFailureException

class GetAllPayouts:
    
    def __init__(
        self,
        payout_repo: IPayoutRepo,
        user_repo: IUserRepo,
    ):
        
        self.payout_repo = payout_repo
        self.user_repo = user_repo
    
    async def execute(
        self,
        payout_filter: PayoutFilter,
    ) -> list:
        
        try:
            if payout_filter.page:
                payout_filter.page = payout_filter.page if payout_filter.page > 0 else 1
            
            payouts_list: list[PayoutModel] = await self.payout_repo.get_all_by_filter(payout_filter)
            
            payouts_number = await self.payout_repo.count_by_filter(payout_filter)
                
            for payout in payouts_list:
                if payout_filter.add_wallet:
                    available, pending = await self.user_repo.get_available_balance(payout.user_id)
                    payout.availableBalance = available
                    payout.pendingBalance = pending
                    
            return PayoutPaginate(
                page = payout_filter.page,
                pageSize = self.payout_repo.page_size,
                totalPages = -(-payouts_number // self.payout_repo.page_size) if payout_filter.page else 1,
                totalDocs = payouts_number if payout_filter.page else len(payouts_list),
                results = [ p.model_dump(by_alias=True) for p in payouts_list],
            )
        except:
            raise OperationFailureException(500, "Internal server error")  