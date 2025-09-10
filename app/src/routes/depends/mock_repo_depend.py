from app.src.repo.interface.Imock_repo import IMockRepo
from app.src.repo.mongodb.mock_mongodb_repo import MockMongodbRepo

def get_mock_repo() -> IMockRepo:
    return MockMongodbRepo()
