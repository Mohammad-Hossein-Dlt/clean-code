from app.src.models.schemas.user.create_user_input import CreateUserInput
from app.src.models.schemas.simple.simple_output import SimpleOutput
from app.src.domain.schemas.user.user_model import UserModel
from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.infra.auth.jwt_handler import JWTHandler
from app.src.domain.schemas.auth.jwt_payload import JWTPayload
from app.src.infra.exception.exceptions import OperationFailureException

class CreateUser:
    
    def __init__(
        self,
        user_repo: IUserRepo,
        jwt_handler: JWTHandler,
    ):
        
        self.user_repo = user_repo
        self.jwt_handler = jwt_handler
    
    async def execute(
        self,
        user: CreateUserInput,
    ) -> SimpleOutput:
        
        try:
            user_data: UserModel = await self.user_repo.insert_user(UserModel.model_validate(user, from_attributes=True))
            return SimpleOutput(message="User registered successfully")
        except:
            raise OperationFailureException(500, "Internal server error")  