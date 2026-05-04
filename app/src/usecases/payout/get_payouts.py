from src.repo.interface.Iuser_repo import IUserRepo
from src.repo.interface.Iwallet_repo import IWalletRepo
from src.repo.interface.Ipayout_repo import IPayoutRepo
from src.usecases.payout.get_balances import GetBalances
from src.models.filter.payout_sriteria import PayoutCriteria
from src.models.schemas.payout.payout_paginate import PayoutPaginate
from src.domain.schemas.payout.payout_model import PayoutModel
from src.infra.exceptions.exceptions import AppBaseException, OperationFailureException

class GetPayouts:
    
    def __init__(
        self,
        user_repo: IUserRepo,
        wallet_repo: IWalletRepo,
        payout_repo: IPayoutRepo,
    ):
        
        self.user_repo = user_repo
        self.payout_repo = payout_repo
        self.wallet_repo = wallet_repo
        self.get_balances = GetBalances(user_repo, wallet_repo)
    
    async def execute(
        self,
        criteria: PayoutCriteria,
    ) -> PayoutPaginate:
        
        try:
            if criteria.page:
                criteria.page = criteria.page if criteria.page > 0 else 1
            
            payouts_list: list[PayoutModel] = await self.payout_repo.get_by_criteria(criteria)
            
            payouts_number = await self.payout_repo.count_by_criteria(criteria)
                
            if criteria.add_wallet:
                for payout in payouts_list:
                    available, pending = await self.get_balances.execute(payout.user_id)
                    payout.availableBalance = available
                    payout.pendingBalance = pending
                    
            return PayoutPaginate(
                page = criteria.page,
                pageSize = criteria.limit,
                totalPages = -(-payouts_number // criteria.limit) if criteria.limit else 1,
                totalDocs = payouts_number if criteria.limit else len(payouts_list),
                results = [ p.model_dump(by_alias=True, mode="json") for p in payouts_list],
            )
        except AppBaseException:
            raise
        except:
            raise OperationFailureException(500, "Internal server error")  