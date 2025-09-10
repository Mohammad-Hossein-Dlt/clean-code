from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.src.infra.settings.settings import settings
from app.src.infra.db.mongodb.client import init_mongodb
from .app_state import AppStates, set_app_state

@asynccontextmanager
async def lifespan(app: FastAPI):
            
    await init_mongodb(
        host=settings.MONGO_HOST,
        port=settings.MONGODB_PORT,
        username=settings.MONGO_INITDB_ROOT_USERNAME,
        password=settings.MONGO_INITDB_ROOT_PASSWORD,
        db_name=settings.MONGO_INITDB_DATABASE
    )
    
    set_app_state(app, AppStates.JWT_SECRET.value, settings.JWT_SECRET)
    set_app_state(app, AppStates.JWT_ALGORITHM.value, settings.JWT_ALGORITHM)
    set_app_state(app, AppStates.JWT_EXPIRATION_MINUTES.value, settings.JWT_EXPIRATION_MINUTES)
    set_app_state(app, AppStates.DEFAULT_PAGE_SIZE.value, settings.DEFAULT_PAGE_SIZE)
            
    yield    
