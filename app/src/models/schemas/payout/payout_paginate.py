from pydantic import BaseModel
from app.src.domain.schemas.payout.payout_model import PayoutModel

class PayoutPaginate(BaseModel):
    page: int | None = None
    pageSize: int | None = None
    totalPages: int | None = None
    totalDocs: int | None = None
    results: list[PayoutModel] | None = None
    