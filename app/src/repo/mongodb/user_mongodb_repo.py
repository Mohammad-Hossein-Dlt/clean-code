from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.domain.schemas.user.user_model import UserModel
from app.src.domain.schemas.user.wallet_model import WalletModel, TransactionModel
from app.src.infra.db.mongodb.collections.user_collection import UserCollection
from app.src.infra.db.mongodb.collections.wallet_collection import WalletCollection
from bson.objectid import ObjectId
from beanie.operators import And
from datetime import datetime, timezone

class UserMongodbRepo(IUserRepo):
            
    async def insert_user(
        self,
        user: UserModel,
    ) -> UserModel:
        
        check_user_with_username = await self.get_user_by_username(user.email)
        check_user_with_email = await self.get_user_by_email(user.email)
                
        if check_user_with_username or check_user_with_email:
            return user
        
        insert_new_user = await UserCollection.insert(
            UserCollection(**user.model_dump(exclude={"id", "_id"})),
        )
        return UserModel.model_validate(insert_new_user, from_attributes=True)
    
    async def delete_user(
        self,
        user_id: str,
    ) -> bool:
    
        user = UserCollection.find(UserCollection.id == ObjectId(user_id))                
        wallet = WalletCollection.find(WalletCollection.user_id == ObjectId(user_id))

        delete_wallet = await wallet.delete()
        if delete_wallet.deleted_count > 0:
            delete_user = await user.delete()
            if delete_user.deleted_count > 0:
                return bool(delete_user.deleted_count)
        
        return False
        
    async def get_user_by_id(
        self,
        user_id: str,
    ) -> UserModel:
    
        user = await UserCollection.get(user_id)
        
        if not user:
            return None
        
        return UserModel.model_validate(user, from_attributes=True)
    
    async def get_user_by_username(
        self,
        username: str,
    ) -> UserModel | None:
    
        user = await UserCollection.find_one(UserCollection.username == username)
        
        if not user:
            return None
        
        return UserModel.model_validate(user, from_attributes=True)
    
    async def get_user_by_email(
        self,
        email: str,
    ) -> UserModel | None:
    
        user = await UserCollection.find_one(UserCollection.email == email)
        
        if not user:
            return None
        
        return UserModel.model_validate(user, from_attributes=True)
        
    async def get_all_users(
        self,
    ) -> list[UserModel]:
    
        users = await UserCollection.find_all().to_list()
        return [UserModel.model_validate(user, from_attributes=True) for user in users ]
    
    async def insert_user_wallet(
        self,
        wallet: WalletModel,
    ) -> WalletModel:
    
        user_wallet = await WalletCollection.insert(
            WalletCollection(**wallet.model_dump())
        )
        return WalletModel.model_validate(user_wallet, from_attributes=True)
    
    async def get_all_user_wallets(
        self,
        user_id: str,
    ) -> list[WalletModel]:
    
        all_wallets = await WalletCollection.find(WalletCollection.user_id == ObjectId(user_id)).to_list()
                
        if not all_wallets:
            return None
        
        return [ WalletModel.model_validate(wallet, from_attributes=True) for wallet in all_wallets]
    
    async def add_transaction(
        self,
        user_id: str,
        wallet_id: str,
        transaction: TransactionModel,
    ) -> WalletModel:
    
        wallet = await WalletCollection.find_one(
            And(
                WalletCollection.id == ObjectId(wallet_id),
                WalletCollection.user_id == ObjectId(user_id),
            ),
        )
        
        if not wallet:
            return None
        
        wallet.transactions.append(transaction)
        wallet.updated = transaction.created
        await wallet.save()
        return wallet

    async def get_balances(
        self,
        user_id: str,
    ) -> tuple[float, float]:
        
        all_wallets = await WalletCollection.find(WalletCollection.user_id == ObjectId(user_id)).to_list()
        
        total_available_balance = 0
        total_pending_balance = 0
        for wallet in all_wallets:
            
            transactions_to_delete = []
            
            for trns in wallet.transactions:
                if trns.date_available.astimezone(timezone.utc) <= datetime.now(timezone.utc):
                    wallet.available_balance += trns.amount
                    transactions_to_delete.append(str(trns.id))
                else:
                    wallet.pending_balance += trns.amount
                        
            wallet.transactions = [trns for trns in wallet.transactions if str(trns.id) not in transactions_to_delete]            
            await wallet.save()
            
            total_available_balance += wallet.available_balance
            total_pending_balance += wallet.pending_balance
            
            if wallet.user_id == ObjectId("68c46856aece80c81d38b439"):
                print(total_available_balance)
                print(total_pending_balance)
        
        
        return total_available_balance, total_pending_balance