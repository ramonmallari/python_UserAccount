class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate = int_rate
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < 0:
            print("Insufficient funds: $5 dollar fee.")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}, Interest rate: {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.interest_yield = self.balance * self.int_rate
            self.balance += self.interest_yield
        return self


class User:
    def __init__(self, name, email,int_rate=0, balance=0):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate, balance)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"User {self.name}")
        self.account.display_account_info()



account_one = User("Ramon O. Mallari", "ramon.mallari@gmail.com", .02)
account_one.make_deposit(1200).make_deposit(5000).make_withdrawal(325).display_user_balance()

account_two = User("Kristine May P. Mallari", "kristinemaypinsan@gmail.com", .5)
account_two.make_deposit(2000).make_deposit(915).make_withdrawal(25).make_withdrawal(60).make_withdrawal(50).make_withdrawal(35).display_user_balance()