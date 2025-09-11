from pymongo import AsyncMongoClient
from beanie import init_beanie
from .collections.user_collection import UserCollection
from .collections.wallet_collection import WalletCollection
from .collections.payout_collection import PayoutCollection


async def init_mongodb(
    host: str,
    port: int,
    username: str,
    password: str,
    db_name: str
):
    
    client = AsyncMongoClient(
        host=host,
        port=port,
        username=username,
        password=password
    )
    
    await init_beanie(
        database=client[db_name],
        document_models=[
            UserCollection,
            WalletCollection,
            PayoutCollection,
        ],
    )