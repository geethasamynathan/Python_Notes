import unittest
from bank_account import BankAccount
class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        """
        This method runs before every test case. It sets up a fresh account.
        """
        self.account = BankAccount("John Doe", 100.0)  # Initial balance is 100

    def test_deposit_valid(self):
        """
        Test case for depositing a valid amount.
        """
        self.assertEqual(self.account.deposit(50), 150)  # Balance should be 150

    def test_deposit_invalid(self):
        """
        Test case for depositing a negative amount, which should raise an error.
        """
        with self.assertRaises(ValueError):
            self.account.deposit(-20)

    def test_withdraw_valid(self):
        """
        Test case for withdrawing a valid amount.
        """
        self.assertEqual(self.account.withdraw(30), 70)  # Balance should be 70

    def test_withdraw_insufficient_funds(self):
        """
        Test case for withdrawing an amount greater than the balance.
        """
        with self.assertRaises(ValueError):
            self.account.withdraw(200)  # Should raise an error

    def test_withdraw_negative_amount(self):
        """
        Test case for withdrawing a negative amount.
        """
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

if __name__ == '__main__':
    unittest.main()