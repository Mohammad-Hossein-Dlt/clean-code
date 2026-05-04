from abc import ABC, abstractmethod
from src.domain.schemas.user.user_model import UserModel
from src.models.filter.base_filter_criteria import BaseFilterCriteria

class IUserRepo(ABC):
    
    @abstractmethod
    def create_mock(
        user: UserModel,
    ) -> UserModel:
    
        raise NotImplementedError
    
    @abstractmethod
    def create(
        user: UserModel,
    ) -> UserModel:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(
        user_id: str,
    ) -> UserModel:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_by_username(
        username: str,
    ) -> UserModel:
    
        raise NotImplementedError
    
    @abstractmethod
    def get_by_email(
        email: str,
    ) -> UserModel:
    
        raise NotImplementedError
    
    @abstractmethod
    def update(
        user: UserModel,
    ) -> UserModel:
    
        raise NotImplementedError
    
    @abstractmethod
    def delete_by_id(
        user_id: str,
    ) -> bool:
    
        raise NotImplementedError
        
    @abstractmethod
    def get_all(
        criteria: BaseFilterCriteria | None = None, 
    ) -> list[UserModel]:
        raise NotImplementedError
    
    @abstractmethod
    def delete_all(
        user_id: str,
    ) -> bool:
    
        raise NotImplementedError