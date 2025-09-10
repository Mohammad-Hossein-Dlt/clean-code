from beanie import Document
from app.src.domain.schemas.payout.payout_model import PayoutModel
from app.src.domain.filter.payout_filter import PayoutFilter


class PayoutSession(PayoutModel, Document):
    class Settings:
        name = "Payout"
        
    @classmethod
    def create_query_by_filter(
        cls,
        payout_filter: PayoutFilter,
    ):
        
        query = {}

        if payout_filter.start_date:
            query[str(cls.created)] = {"$gte": payout_filter.start_date}

        if payout_filter.end_date:
            query.setdefault(str(cls.created), {})
            query[str(cls.created)]["$lte"] = payout_filter.end_date

        if payout_filter.payment_start_date:
            query[str(cls.payment_date)] = {"$gte": payout_filter.payment_start_date}

        if payout_filter.payment_end_date:
            query.setdefault(str(cls.payment_date), {})
            query[str(cls.payment_date)]["$lte"] = payout_filter.payment_end_date

        if payout_filter.user_type:
            query[str(cls.user_type)] = payout_filter.user_type.value

        if payout_filter.statuses:
            query[str(cls.status)] = {"$in": payout_filter.statuses}
                    
        return query