from src.repo.interface.Ipayout_repo import IPayoutRepo
from src.domain.schemas.payout.payout_model import PayoutModel
from src.infra.database.mongodb.collections.payout_collection import PayoutCollection
from src.models.filter.base_filter_criteria import BaseFilterCriteria
from app.src.models.filter.payout_filter_input import PayoutFilterInput
from src.infra.exceptions.exceptions import EntityNotFoundError
from src.infra.utils.convert_id import convert_database_id

class PayoutMongodbRepo(IPayoutRepo):

    async def create_mock(
        self,
        payout: PayoutModel,
    ) -> PayoutModel:
                
        try:
            new_payout = await PayoutCollection.insert(
                PayoutCollection(**payout.model_dump_for_mock()),
            )
            return PayoutModel.model_validate(new_payout, from_attributes=True) 
        except:
            raise
        
    async def create(
        self,
        payout: PayoutModel,
    ) -> PayoutModel:
                
        try:
            new_payout = await PayoutCollection.insert(
                PayoutCollection(**payout.model_dump_for_create()),
            )
            return PayoutModel.model_validate(new_payout, from_attributes=True) 
        except:
            raise
        
    async def get_by_id(
        self,
        payout_id: str,
    ) -> PayoutModel:
    
        try:
            payout_id = convert_database_id(payout_id)
            payout = await PayoutCollection.find(
                PayoutCollection.id == payout_id,
            ).to_list()
            return PayoutModel.model_validate(payout, from_attributes=True)
        except:
            raise EntityNotFoundError(status_code=404, message=f"No Payout exist for user this user")
        
    async def update(
        self,
        payout: PayoutModel,
    ) -> PayoutModel:
    
        try:               
            
            to_update: dict = PayoutModel.model_dump_for_update(
                exclude_none=True,
                db_stack="no-sql",
            )
            
            await PayoutCollection.find(
                PayoutCollection.id == payout.id,
            ).update(
                {
                    "$set": to_update,
                },
            )
                        
            return await self.get_by_id(payout.id)
        except EntityNotFoundError:
            raise
        
    async def delete_by_id(
        self,
        payout_id: str,
    ) -> bool:
    
        try:
            payout_id = convert_database_id(payout_id)
            delete_payout = await PayoutCollection.find_one(
                PayoutCollection.id == payout_id,
            ).delete()
            return bool(delete_payout.deleted_count)
        except:
            raise EntityNotFoundError(status_code=404, message="Payout not found")
        
    async def get_by_user_id(
        self,
        user_id: str,
        criteria: BaseFilterCriteria | None = None, 
    ) -> list[PayoutModel]:
    
        try:
            user_id = convert_database_id(user_id)
            query = PayoutCollection.find(
                PayoutCollection.user_id == user_id,
            )            
            if criteria:
                query.skip(
                    criteria.page * criteria.limit
                ).limit(
                    criteria.limit
                ).sort(
                    PayoutCollection.created_at if criteria.order == "asc" else -PayoutCollection.created_at
                )
            
            payouts_list = await query.to_list()
            
            return [ PayoutModel.model_validate(payout, from_attributes=True) for payout in payouts_list]
        except:
            raise EntityNotFoundError(status_code=404, message=f"No payout exist for user this user")
        
    async def delete_by_user_id(
        self,
        user_id: str,
    ) -> bool:
    
        try:
            user_id = convert_database_id(user_id)
            delete_payouts = await PayoutCollection.find(
                PayoutCollection.user_id == user_id,
            ).delete()
            return bool(delete_payouts.deleted_count)
        except:
            raise EntityNotFoundError(status_code=404, message="Wallet not found")

    async def count_by_criteria(
        self,
        criteria: PayoutFilterInput,
    ) -> int:
        
        try:
            query = PayoutCollection.create_query_by_criteria(criteria)
            docs_number = await PayoutCollection.find(query).count()
            return docs_number
        except:
            raise EntityNotFoundError(status_code=404, message="Wallet not found")
        
    async def get_by_criteria(
        self,
        criteria: PayoutFilterInput,
    ) -> list[PayoutModel]:
        
        try:
            query = PayoutCollection.create_query_by_criteria(criteria)
            query = PayoutCollection.find(query)            
            if criteria:
                query.skip(
                    criteria.page * criteria.limit
                ).limit(
                    criteria.limit
                ).sort(
                    PayoutCollection.created_at if criteria.order == "asc" else -PayoutCollection.created_at
                )
            
            payouts_list = await query.to_list()
            
            return [ PayoutModel.model_validate(payout, from_attributes=True) for payout in payouts_list]
        except:
            raise EntityNotFoundError(status_code=404, message=f"No payout exist for user this user")

    async def delete_all(
        self,
    ) -> bool:
    
        try:
            delete_payouts = await PayoutCollection.find_all().delete()
            return bool(delete_payouts.deleted_count)
        except:
            raise EntityNotFoundError(status_code=404, message="Wallet not found")