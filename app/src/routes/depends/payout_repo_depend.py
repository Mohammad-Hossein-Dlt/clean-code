from app.src.infra.fastapi_config.app import app
from app.src.infra.fastapi_config.app_state import AppStates, get_app_state
from app.src.repo.interface.Ipayout_repo import IPayoutRepo
from app.src.repo.mongodb.payout_mongodb_repo import PayoutMongodbRepo

def get_payout_repo() -> IPayoutRepo:
    page_size = get_app_state(app, AppStates.DEFAULT_PAGE_SIZE)
    return PayoutMongodbRepo(page_size=page_size)
