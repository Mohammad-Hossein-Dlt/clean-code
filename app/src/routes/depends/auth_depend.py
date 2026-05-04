from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.infra.context.app_context import AppContext
from src.domain.schemas.user.user_model import UserModel
from src.infra.bootstrap.jwt_handler import JWTHandler
from src.usecases.user.user.get_by_id import GetUser
from src.domain.enums import UserType
from src.infra.exceptions.exceptions import AppBaseException
from src.repo.interface.Iuser_repo import IUserRepo
from .repo_depend import get_user_repo

schema = OAuth2PasswordBearer(tokenUrl="/api_v1/user/login")

def get_jwt_depend() -> JWTHandler:
    return AppContext.jwt

async def get_authenticated_token_payload(
    jwt_handler: JWTHandler = Depends(get_jwt_depend),
    token: str = Depends(schema),
    user_repo: IUserRepo = Depends(get_user_repo),
) -> UserModel:
    
    try:
        payload = jwt_handler.decode_jwt_token(token)
    except AppBaseException as ex:
        raise HTTPException(status_code=ex.status_code, detail=ex.message)
    
    if jwt_handler.is_token_valid(payload.model_dump()):
        
        try:
            get_user_usecase = GetUser(user_repo)
            user = await get_user_usecase.execute(payload.user_id)
            if user:
                return payload
        except:        
            raise HTTPException(status_code=404, detail="User not found")
    
    raise HTTPException(status_code=401, detail="Token expired")

def check_admin_access(
    payload: UserModel = Depends(get_authenticated_token_payload)
):
    if payload.user_type != UserType.admin.value:
        raise HTTPException(status_code=403, detail="Access denied. You are not admin")