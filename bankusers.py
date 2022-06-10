# 1.Update the User class __init__ method

# 2.Update the User class make_deposit method

# 3.Update the User class make_withdrawal method

# 4.Update the User class display_user_balance method

# 5.SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

class BankAccount:
    bank_name = "First national Bank"
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficient funds:Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self

    def user_account(self, user):
        self.user_account = user
        print(f"User: {self.name}, balance: {self.amount}")


class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.account = BankAccount(0.02, 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        self.display_user_balance()
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        self.display_user_balance()
        return self

    def display_account_info(self, amount):
        self.account.display_account_info()
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")


guido = User("Guido van Rossum")
monty = User("Monty Python")
guido.make_withdraw(600)
guido.make_withdraw(25)
guido.make_deposit(20)
guido.make_deposit(600)

monty.make_deposit(200)
monty.make_deposit(39)
monty.make_withdraw(28)
monty.make_withdraw(120)
