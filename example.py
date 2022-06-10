class User:
    # other methods
    def make_deposit(self, amount):
        # hmmm...the User class doesn't have an account_balance attribute anymore
        self.account_balance += amount


class User:
    def example_method(self):
        # we can call the BankAccount instance's methods
        self.account.deposit(100)
        print(self.account.balance)		# or access its attributes
