from src.repo.interface.Iwallet_repo import IWalletRepo
from src.models.schemas.user.update_user_input import UpdateUserInput
from src.domain.schemas.user.user_model import UserModel
from src.infra.exceptions.exceptions import AppBaseException, OperationFailureException

class UpdateWallet:
    
    def __init__(
        self,
        wallet_repo: IWalletRepo,
    ):
        
        self.user_repo = wallet_repo
    
    async def execute(
        self,
        entity: UpdateUserInput,
    ) -> UserModel:
        
        try:
            user_model: UserModel = UserModel.model_validate(entity, from_attributes=True)
            return await self.user_repo.update(user_model)
        except AppBaseException:
            raise
        except:
            raise OperationFailureException(500, "Internal server error")  