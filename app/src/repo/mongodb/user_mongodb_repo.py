from app.src.domain.schemas.user.user_model import UserModel
from app.src.domain.schemas.user.wallet_model import TransactionModel, WalletModel
from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.infra.db.mongodb.sessions.user_session import UserSession
from app.src.infra.db.mongodb.sessions.wallet_session import WalletSession
from bson.objectid import ObjectId
from datetime import datetime, timezone

class UserMongodbRepo(IUserRepo):
            
    async def insert_user(self, user: UserModel) -> UserModel:
        
        check_user_with_username = await self.get_user_by_username(user.email)
        check_user_with_email = await self.get_user_by_email(user.email)
                
        if check_user_with_username or check_user_with_email:
            return user
        
        insert_new_user = await UserSession.insert(
            UserSession(**user.model_dump(exclude={"id", "_id"})),
        )
        return UserModel.model_validate(insert_new_user, from_attributes=True)
    
    async def delete_user(self, user_id: str) -> bool:
        user = await UserSession.get(user_id)        
        if not user:
            return False
        
        wallet = await WalletSession.find_one(WalletSession.user_id == ObjectId(user_id))
        if not wallet:
            delete_user = await user.delete()
            return bool(delete_user.deleted_count)
        
        delete_wallet = await wallet.delete()
        if delete_wallet.deleted_count == 1:
            delete_user = await user.delete()
            return bool(delete_user.deleted_count)
        
        return False
        
    async def get_user_by_id(self, user_id: str) -> UserModel:
        user = await UserSession.get(user_id)
        
        if not user:
            return None
        
        return UserModel.model_validate(user, from_attributes=True)
    
    async def get_user_by_username(self, username: str) -> UserModel | None:
        user = await UserSession.find_one(UserSession.username == username)
        
        if not user:
            return None
        
        return UserModel.model_validate(user, from_attributes=True)
    
    async def get_user_by_email(self, email: str) -> UserModel | None:
        user = await UserSession.find_one(UserSession.email == email)
        
        if not user:
            return None
        
        return UserModel.model_validate(user, from_attributes=True)
        
    async def get_all_users(self) -> list[UserModel]:
        users = await UserSession.find_all().to_list()
        return [UserModel.model_validate(user, from_attributes=True) for user in users ]
    
    async def insert_user_wallet(self, wallet: WalletModel) -> WalletModel:
        user_wallet = await WalletSession.insert(
            WalletSession(**wallet.model_dump())
        )
        return WalletModel.model_validate(user_wallet, from_attributes=True)
    
    async def get_user_wallet(self, user_id: str) -> WalletModel:
        wallet = await WalletSession.find_one(WalletSession.user_id == ObjectId(user_id))
                
        if not wallet:
            return None
        
        return WalletModel.model_validate(wallet, from_attributes=True)
    
    async def add_transaction(self, user_id: str, transaction: TransactionModel) -> WalletModel:
        wallet = await WalletSession.find_one(WalletSession.user_id == ObjectId(user_id))
        wallet.transactions.append(transaction)
        wallet.updated = datetime.now(timezone.utc)
        await wallet.save()
        return wallet

    async def get_available_balance(
        self,
        user_id: str,
    ) -> tuple[float, float]:
        
        wallet = await WalletSession.find_one(WalletSession.user_id == ObjectId(user_id))
        
        if not wallet:
            return 0, 0

        available_balance = wallet.available_balance
        pending_balance = 0
        transactions_to_delete = []

        for trns in wallet.transactions:
            if trns.date_available.time() <= datetime.now(timezone.utc).time():
                available_balance += trns.amount
                transactions_to_delete.append(trns)
            else:
                pending_balance += trns.amount

        wallet.available_balance = available_balance
        wallet.pending_balance = pending_balance
        wallet.transactions = [trns for trns in wallet.transactions if trns not in transactions_to_delete]
        await wallet.save()
        
        return available_balance, pending_balance