from abc import ABC, abstractmethod
from src.domain.schemas.user.user_model import UserModel

class IMockRepo(ABC):
       
    @abstractmethod
    def delete_mock_data(
        users: list[UserModel],
    ) -> bool:
    
        raise NotImplementedError    
    
    
