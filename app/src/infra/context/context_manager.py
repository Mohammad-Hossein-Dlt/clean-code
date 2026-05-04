from .app_context import AppContext
from src.infra.settings.settings import settings
from src.infra.bootstrap.jwt_handler import JWTHandler
from src.infra.bootstrap.database import init_database_client, terminate_database_client

class AppContextManager:
        
    @classmethod
    def init_context(cls):
        
        AppContext.environment = settings.ENVIRONMENT
        AppContext.jwt = JWTHandler(settings.JWT.secret, settings.JWT.algorithm, settings.JWT.expiration)
        
    @classmethod
    async def lazy_init_context(cls):
        
        print("     Starting up...     ")
        
        AppContext.db_client = await init_database_client(settings.MONGODB)        

    @classmethod
    async def terminate_context(cls):
        
        print("     Shutting down...     ")
        
        await terminate_database_client(AppContext.db_client)

AppContextManager.init_context()