from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):   
    
    MONGODB_PORT: int     
    
    MONGO_HOST: str
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_DATABASE: str
    
    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXPIRATION_MINUTES: int
    
    DEFAULT_PAGE_SIZE: int
        
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings: Settings = Settings()
