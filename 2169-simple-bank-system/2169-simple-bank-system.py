class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        self.n = len(balance)  # Number of accounts

    def _is_valid(self, account):
        """
        Helper function to check if an account number is valid.
        """
        return 1 <= account <= self.n

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if not self._is_valid(account1) or not self._is_valid(account2):
            return False  # Invalid accounts
        
        if self.balance[account1 - 1] < money:
            return False  # Insufficient funds

        # Perform transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self._is_valid(account):
            return False  # Invalid account

        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self._is_valid(account) or self.balance[account - 1] < money:
            return False  # Invalid account or insufficient funds

        self.balance[account - 1] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)