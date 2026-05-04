from src.repo.interface.Imock_repo import IMockRepo
from src.repo.mongodb.mock_repo import MockMongodbRepo

from src.repo.interface.Iuser_repo import IUserRepo
from src.repo.mongodb.user_repo import UserMongodbRepo

from src.repo.interface.Iwallet_repo import IWalletRepo
from src.repo.mongodb.wallet_repo import WalletMongodbRepo

from src.repo.interface.Ipayout_repo import IPayoutRepo
from src.repo.mongodb.payout_repo import PayoutMongodbRepo

def get_mock_repo() -> IMockRepo:
    return MockMongodbRepo()

def get_user_repo() -> IUserRepo:
    return UserMongodbRepo()

def get_wallet_repo() -> IWalletRepo:
    return WalletMongodbRepo()

def get_payout_repo() -> IPayoutRepo:
    return PayoutMongodbRepo()
