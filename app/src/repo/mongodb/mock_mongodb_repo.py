from app.src.domain.schemas.user.user_model import UserModel
from app.src.domain.schemas.user.wallet_model import WalletModel
from app.src.domain.schemas.payout.payout_model import PayoutModel
from app.src.infra.db.mongodb.sessions.user_session import UserSession
from app.src.infra.db.mongodb.sessions.wallet_session import WalletSession
from app.src.infra.db.mongodb.sessions.payout_session import PayoutSession
from app.src.repo.interface.Imock_repo import IMockRepo
from app.src.infra.db.mongodb.sessions.payout_session import PayoutSession
from beanie.operators import In

class MockMongodbRepo(IMockRepo):
    
    
    async def insert_many_users(
        self,
        users: list[UserModel]
    ) -> list[str]:

        users_session = [ UserSession.model_validate(u, from_attributes=True) for u in users]
        
        try:
            insert = await UserSession.insert_many(users_session)
            return [ str(_id) for _id in insert.inserted_ids]
        except:
            return [ str(u.id) for u in users]
    
    async def insert_many_wallets(
        self,
        wallets: list[WalletModel]
    ) -> list[str]:
            
        wallets_session = [ WalletSession.model_validate(w, from_attributes=True) for w in wallets]

        try:
            insert = await WalletSession.insert_many(wallets_session)
            return [ str(_id) for _id in insert.inserted_ids]
        except:
            return [ str(w.id) for w in wallets]
    
    async def insert_many_payout(
        self,
        payouts: list[PayoutModel]
    ) -> list[str]:

        payouts_session = [ PayoutSession.model_validate(p, from_attributes=True) for p in payouts]

        try:
            insert = await PayoutSession.insert_many(payouts_session)
            return [ str(_id) for _id in insert.inserted_ids]
        except:
            return [ str(p.id) for p in payouts]
    
    async def delete_mock_data(
        self,
        users: list[UserModel],
    ) -> bool:
        
        users_id = [ u.id for u in users ]
        
        get_users = UserSession.find(
            In(
                UserSession.id,
                users_id,
            )
        )
        
        get_wallets = WalletSession.find(
            In(
                WalletSession.user_id,
                users_id,
            )
        )
        
        get_payouts = PayoutSession.find(
            In(
                PayoutSession.user_id,
                users_id,
            )
        )
        
        await get_users.delete()
        await get_wallets.delete()
        await get_payouts.delete()
        
        return True
    
