from app.src.repo.interface.Iuser_repo import IUserRepo
from app.src.repo.mongodb.user_mongodb_repo import UserMongodbRepo

def get_user_repo() -> IUserRepo:
    return UserMongodbRepo()
