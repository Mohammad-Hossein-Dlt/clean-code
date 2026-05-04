from src.repo.interface.Iuser_repo import IUserRepo
from src.infra.bootstrap.jwt_handler import JWTHandler
from src.models.schemas.user.login_user_input import LoginUserInput
from src.models.schemas.user.login_user_output import LoginUserOutput
from src.domain.schemas.user.user_model import UserModel
from src.domain.schemas.auth.jwt_payload import JWTPayload
from src.infra.exceptions.exceptions import AppBaseException, AuthenticationException, OperationFailureException

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
        entity: LoginUserInput,
    ) -> LoginUserOutput:
        
        try:        
            user: UserModel = await self.user_repo.get_by_username(entity.username)

            if not entity.password == user.password:
                raise AuthenticationException(status_code=400, message="Invalid credentials")
            
            payload = JWTPayload(
                user_id=str(user.id),
                user_type=user.user_type,
            )
            
            token = self.jwt_handler.create_jwt_token(payload)
            
            return LoginUserOutput(access_token=token)
        except AppBaseException:
            raise
        except:
            raise OperationFailureException(500, "Internal server error")  