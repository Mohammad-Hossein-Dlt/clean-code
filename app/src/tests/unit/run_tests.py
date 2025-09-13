import unittest

# Domain test cases 
from .domain.test_user_model import UserModelTestExample
from .domain.test_wallet_model import WalletModelTestExample
from .domain.test_payout_model import PayoutModelTestExample
from .domain.test_jwt_payload_model import JWTPayloadModelTestExample

# # Models test cases
from .models.test_create_user_input_model import CreateUserInputTestExample
from .models.test_login_user_input_model import LoginUserInputTestExample
from .models.test_login_user_output_model import LoginUserOutputTestExample
from .models.test_payout_filter_model import PayoutFilterTestExample
from .models.test_payout_paginate_model import PayoutPaginateTestExample
from .models.test_simple_output_model import SimpleOutputTestExample
from .models.test_user_transaction_input_model import UserTransactionInputTestExample

if __name__ == "__main__":
    unittest.main()