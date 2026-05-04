from src.repo.interface.Imock_repo import IMockRepo
from src.domain.schemas.user.user_model import UserModel
from src.infra.database.mongodb.collections.user_collection import UserCollection
from src.infra.database.mongodb.collections.wallet_collection import WalletCollection
from src.infra.database.mongodb.collections.payout_collection import PayoutCollection
from beanie.operators import In

class MockMongodbRepo(IMockRepo):
    
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
    
