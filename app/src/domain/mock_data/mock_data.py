import random
from app.src.domain.schemas.user.user_model import UserModel
from app.src.domain.schemas.user.wallet_model import TransactionModel, WalletModel
from app.src.domain.schemas.payout.payout_model import PayoutModel
from app.src.domain.enums import PaymentMethod, PayoutStatus, UserType
from datetime import datetime, timezone, timedelta
from faker import Faker

faker = Faker()

def create_mock_data(
    mock_users_number: int = 5,
) -> tuple[
    list[UserModel],
    list[WalletModel],
    list[PayoutModel],
]:
    
    now = datetime.now(timezone.utc)
    
    start_date = now - timedelta(days=30)
    end_date = now + timedelta(days=30)
    
    users = [
        UserModel(
            name=faker.name(),
            email=faker.email(),
            username=faker.user_name(),
            password=faker.password(),
            user_type=random.choice([UserType.reqular, UserType.admin]),
            created=faker.date_time_between(start_date=start_date, end_date=now, tzinfo=timezone.utc),
        ) for _ in range(mock_users_number)
    ]

    wallets = []
    payouts = []

    for user in users:
        
        wallet = WalletModel(
            user_id=user.id,
            created=user.created,
        )
        
        transactions = [
            TransactionModel(
            amount=round(random.uniform(50, 500), 2),
            date_available=faker.date_time_between(start_date=wallet.created, end_date=end_date, tzinfo=timezone.utc)
            ) for _ in range(random.randint(1, 5))
        ]
                
        wallet.transactions = transactions
        
        wallets.append(wallet)
        
        payout = PayoutModel(
            user_id=user.id,
            user_type=user.user_type,
            amount=round(random.uniform(50, wallet.available_balance), 2),
            status=random.choice([PayoutStatus.pending, PayoutStatus.approved, PayoutStatus.paid, PayoutStatus.rejected]),
            payment_method=random.choice([PaymentMethod.bank, PaymentMethod.paypal, PaymentMethod.crypto]),
            payment_date=faker.date_time_between(start_date=wallet.created, end_date=end_date, tzinfo=timezone.utc),
            created=faker.date_time_between(start_date=wallet.created, end_date=end_date, tzinfo=timezone.utc)
        )
        payouts.append(payout)
    
    return users, wallets, payouts


mock_users, mock_wallets, mock_payouts = create_mock_data(5)