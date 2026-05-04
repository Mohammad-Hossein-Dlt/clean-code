from src.domain.enums import Environment
from src.infra.schemas.database.mongodb import MongodbParams
from src.infra.schemas.jwt.jwt_params import JwtParams
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
       
    ENVIRONMENT: Environment
    MONGODB: MongodbParams
    JWT: JwtParams
        
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=[
            f".env.{os.getenv("ENVIRONMENT", "dev")}",
            f"../.env.{os.getenv("ENVIRONMENT", "dev")}",
        ],
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )


settings: Settings = Settings()
