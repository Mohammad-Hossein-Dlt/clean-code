import unittest
from .test_user_model import UserTestExample
from .test_wallet_model import WalletTestExample
from .test_payout_model import PayoutTestExample

if __name__ == "__main__":
    '''
    To run:    
    python -m app.src.tests.unit.run_tests
    '''    

    unittest.main()