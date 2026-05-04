from src.models.schemas.user.update_user_input import UpdateUserInput
from src.domain.schemas.user.user_model import UserModel
from src.repo.interface.Iuser_repo import IUserRepo
from src.infra.exceptions.exceptions import AppBaseException, OperationFailureException
from src.infra.utils.convert_id import convert_object_id

class UpdateUser:
    
    def __init__(
        self,
        user_repo: IUserRepo,
    ):
        
        self.user_repo = user_repo
    
    async def execute(
        self,
        user_id: str,
        entity: UpdateUserInput,
    ) -> UserModel:
        
        try:
            user_model: UserModel = UserModel.model_validate(entity, from_attributes=True)
            user_model.id = convert_object_id(user_id)
            return await self.user_repo.update(user_model)
        except AppBaseException:
            raise
        except:
            raise OperationFailureException(500, "Internal server error")  