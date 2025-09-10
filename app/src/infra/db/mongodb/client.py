from pymongo import AsyncMongoClient
from beanie import init_beanie
from .sessions.user_session import UserSession
from .sessions.wallet_session import WalletSession
from .sessions.payout_session import PayoutSession


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
            UserSession,
            WalletSession,
            PayoutSession,
        ],
    )