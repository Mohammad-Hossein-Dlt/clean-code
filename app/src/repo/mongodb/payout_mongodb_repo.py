from app.src.repo.interface.Ipayout_repo import IPayoutRepo
from app.src.domain.schemas.payout.payout_model import PayoutModel
from app.src.infra.db.mongodb.collections.payout_collection import PayoutCollection
from app.src.models.filter.payout_filter import PayoutFilter

class PayoutMongodbRepo(IPayoutRepo):
    
    def __init__(self, page_size: int):
        super().__init__(page_size)
        
        
    async def count_by_filter(
        self,
        payout_filter: PayoutFilter,
    ) -> int:
        
        query = PayoutCollection.create_query_by_filter(payout_filter)
        
        docs_number = await PayoutCollection.find(query).count()
        
        return docs_number
    
    async def get_all_by_filter(
        self,
        payout_filter: PayoutFilter,
    ) -> list[PayoutModel]:
        
        query = PayoutCollection.create_query_by_filter(payout_filter)
        payouts: list[PayoutCollection] = []
        
        if payout_filter.page is None:
            payouts  = await PayoutCollection.find(query).to_list()
        else:
            skip = (payout_filter.page - 1) * self.page_size
            payouts = await PayoutCollection.find(query).skip(skip).limit(self.page_size).to_list()
        
        if not payouts:
            return []    
        
        return [ PayoutModel.model_validate(payout, from_attributes=True) for payout in payouts ]
    