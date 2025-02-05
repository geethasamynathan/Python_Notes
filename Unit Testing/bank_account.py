class BankAccount:
    def __init__(self, owner, balance=0.0):
        """
        Initializes the bank account with the owner's name and initial balance.
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a given amount to the bank account.
        """
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a given amount from the bank account if sufficient balance exists.
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            return self.balance