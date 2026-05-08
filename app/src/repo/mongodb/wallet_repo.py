from src.repo.interface.Iwallet_repo import IWalletRepo
from src.domain.schemas.user.wallet_model import WalletModel
from src.infra.database.mongodb.collections.wallet_collection import WalletCollection
from src.models.filter.base_filter_criteria import BaseFilterCriteria
from src.infra.exceptions.exceptions import EntityNotFoundError
from src.infra.utils.convert_id import convert_database_id

class WalletMongodbRepo(IWalletRepo):
        
    async def create_mock(
        self,
        wallet: WalletModel,
    ) -> WalletModel:
    
        try:
            user_wallet = await WalletCollection.insert(
                WalletCollection(**wallet.model_dump())
            )
            return WalletModel.model_validate(user_wallet, from_attributes=True)
        except:
            raise
            
    async def create(
        self,
        wallet: WalletModel,
    ) -> WalletModel:
    
        try:
            user_wallet = await WalletCollection.insert(
                WalletCollection(**wallet.model_dump_for_db(dump_for="create"))
            )
            return WalletModel.model_validate(user_wallet, from_attributes=True)
        except:
            raise
    
    async def get_by_id(
        self,
        wallet_id: str,
    ) -> WalletModel:
    
        try:
            wallet_id = convert_database_id(wallet_id)
            wallet = await WalletCollection.find_one(
                WalletCollection.id == wallet_id,
            )
            return WalletModel.model_validate(wallet, from_attributes=True)
        except:
            raise EntityNotFoundError(status_code=404, message="Wallet not found")
        
    async def update(
        self,
        wallet: WalletModel,
    ) -> WalletModel:
    
        try:               
            
            to_update: dict = wallet.model_dump_for_db(
                dump_for="update",
                exclude_none=True,
            )
            
            await WalletCollection.find(
                WalletCollection.id == wallet.id,
            ).update(
                {
                    "$set": to_update,
                },
            )
                        
            return await self.get_by_id(wallet.id)
        except EntityNotFoundError:
            raise
        
    async def delete_by_id(
        self,
        wallet_id: str,
    ) -> bool:
    
        try:
            wallet_id = convert_database_id(wallet_id)
            delete_wallet = await WalletCollection.find_one(
                WalletCollection.id == wallet_id,
            ).delete()
            return bool(delete_wallet.deleted_count)
        except:
            raise EntityNotFoundError(status_code=404, message="Wallet not found")
        
    async def get_by_user_id(
        self,
        user_id: str,
        criteria: BaseFilterCriteria | None = None, 
    ) -> list[WalletModel]:
    
        try:
            user_id = convert_database_id(user_id)
            query = WalletCollection.find(
                WalletCollection.user_id == user_id,
            )
            if criteria:
                query.skip(
                    criteria.page * criteria.limit
                ).limit(
                    criteria.limit
                ).sort(
                    WalletCollection.id if criteria.order == "asc" else -WalletCollection.id
                )
            
            wallets_list = await query.to_list()

            return [ WalletModel.model_validate(wallet, from_attributes=True) for wallet in wallets_list]
        except:
            raise EntityNotFoundError(status_code=404, message="Wallet not found")
        
    async def delete_by_user_id(
        self,
        user_id: str,
    ) -> bool:
    
        try:
            user_id = convert_database_id(user_id)
            delete_wallets = await WalletCollection.find(
                WalletCollection.user_id == user_id,
            ).delete()
            return bool(delete_wallets.deleted_count)
        except:
            raise EntityNotFoundError(status_code=404, message="Wallet not found")
        
    async def get_all(
        self,
        criteria: BaseFilterCriteria | None = None, 
    ) -> list[WalletModel]:
    
        try:
            
            query = WalletCollection.find_all()
            
            if criteria:
                query.skip(
                    criteria.page * criteria.limit
                ).limit(
                    criteria.limit
                ).sort(
                    WalletCollection.id if criteria.order == "asc" else -WalletCollection.id
                )
            
            wallets_list = await query.to_list()
            
            return [ WalletModel.model_validate(wallet, from_attributes=True) for wallet in wallets_list]
        except:
            raise EntityNotFoundError(status_code=404, message="Wallet not found")
        
    async def delete_all(
        self,
    ) -> bool:
    
        try:
            delete_wallets = await WalletCollection.find_all().delete()                
            return bool(delete_wallets.deleted_count)
        except:
            raise EntityNotFoundError(status_code=404, message="User not found")