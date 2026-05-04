from typing import ClassVar
from src.domain.enums import Environment
from src.infra.schemas.database.sqlalchemy import SqlalchemyClient
from src.infra.schemas.database.mongodb import MongodbClient
from src.infra.bootstrap.jwt_handler import JWTHandler

class AppContext(type):
        
    environment: ClassVar[Environment] = None
    db_client: ClassVar[SqlalchemyClient | MongodbClient] = None
    jwt: ClassVar[JWTHandler] = None