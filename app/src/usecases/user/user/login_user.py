from app.src.domain.schemas.user.user_model import UserModel
from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.models.schemas.user.login_user_input import LoginUserInput
from app.src.models.schemas.user.login_user_output import LoginUserOutput
from app.src.infra.auth.jwt_handler import JWTHandler
from app.src.domain.schemas.auth.jwt_payload import JWTPayload
from app.src.infra.exception.exceptions import AuthenticationException, EntityNotFoundError
from app.src.infra.exception.exceptions import OperationFailureException

class LoginUser:
    
    def __init__(
        self,
        user_repo: IUserRepo,
        jwt_handler: JWTHandler,
    ):
        
        self.user_repo = user_repo
        self.jwt_handler = jwt_handler
    
    async def execute(
        self,
        user: LoginUserInput,
    ) -> LoginUserOutput:
        
        try:
            user_data: UserModel = await self.user_repo.get_user_by_username(user.username)
        except:
            raise OperationFailureException(500, "Internal server error")  
        
        if not user_data:
            raise EntityNotFoundError(status_code=404, message="User not found")
        
        if not user_data.password == user.password:
            raise AuthenticationException(status_code=400, message="Invalid credentials")
        
        payload = JWTPayload(
            user_id = str(user_data.id)
        )
        token = self.jwt_handler.create_jwt_token(payload)
        
        return LoginUserOutput(access_token=token)