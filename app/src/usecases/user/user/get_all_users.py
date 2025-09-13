from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.domain.schemas.user.user_model import UserModel
from app.src.infra.exceptions.exceptions import OperationFailureException

class GetAllUsers:
    
    def __init__(
        self,
        user_repo: IUserRepo,
    ):
        
        self.user_repo = user_repo    
    
    async def execute(
        self,
    ) -> list[UserModel]:
        
        try:
            users: list[UserModel] = await self.user_repo.get_all_users()
            return [ u.model_dump(mode="json") for u in users ]
        except:
            raise OperationFailureException(500, "Internal server error")  