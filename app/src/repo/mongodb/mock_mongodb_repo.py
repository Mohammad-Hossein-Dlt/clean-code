from app.src.domain.schemas.user.user_model import UserModel
from app.src.domain.schemas.user.wallet_model import WalletModel
from app.src.domain.schemas.payout.payout_model import PayoutModel
from app.src.infra.db.mongodb.collections.user_collection import UserCollection
from app.src.infra.db.mongodb.collections.wallet_collection import WalletCollection
from app.src.infra.db.mongodb.collections.payout_collection import PayoutCollection
from app.src.repo.interface.Imock_repo import IMockRepo
from app.src.infra.db.mongodb.collections.payout_collection import PayoutCollection
from beanie.operators import In

class MockMongodbRepo(IMockRepo):
    
    
    async def insert_many_users(
        self,
        users: list[UserModel]
    ) -> list[str]:

        users_session = [ UserCollection.model_validate(u, from_attributes=True) for u in users]
        
        try:
            insert = await UserCollection.insert_many(users_session)
            return [ str(_id) for _id in insert.inserted_ids]
        except:
            return [ str(u.id) for u in users]
    
    async def insert_many_wallets(
        self,
        wallets: list[WalletModel]
    ) -> list[str]:
            
        wallets_session = [ WalletCollection.model_validate(w, from_attributes=True) for w in wallets]

        try:
            insert = await WalletCollection.insert_many(wallets_session)
            return [ str(_id) for _id in insert.inserted_ids]
        except:
            return [ str(w.id) for w in wallets]
    
    async def insert_many_payout(
        self,
        payouts: list[PayoutModel]
    ) -> list[str]:

        payouts_session = [ PayoutCollection.model_validate(p, from_attributes=True) for p in payouts]

        try:
            insert = await PayoutCollection.insert_many(payouts_session)
            return [ str(_id) for _id in insert.inserted_ids]
        except:
            return [ str(p.id) for p in payouts]
    
    async def delete_mock_data(
        self,
        users: list[UserModel],
    ) -> bool:
        
        users_id = [ u.id for u in users ]
        
        get_users = UserCollection.find(
            In(
                UserCollection.id,
                users_id,
            )
        )
        
        get_wallets = WalletCollection.find(
            In(
                WalletCollection.user_id,
                users_id,
            )
        )
        
        get_payouts = PayoutCollection.find(
            In(
                PayoutCollection.user_id,
                users_id,
            )
        )
        
        await get_users.delete()
        await get_wallets.delete()
        await get_payouts.delete()
        
        return True
    
