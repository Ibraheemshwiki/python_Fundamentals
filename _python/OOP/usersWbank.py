class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"user: {self.name}, balance: {self.account.display_account_info()}")
        return self
    def transfer_money(self, amount, person):
        self.make_withdrawal(amount)
        person.make_deposit(amount)
        return self

class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate) 
        return self

# ibraheem = BankAccount(0.01, 1000)
# ibraheem.deposit(1900)
# ibraheem.withdraw(900)
# ibraheem.display_account_info()
# ibraheem.yield_interest()
# ibraheem.display_account_info()

Mahmoud = BankAccount(0.03, 55000)
Mahmoud.deposit(200).deposit(700).deposit(600).withdraw(2000).yield_interest().display_account_info()

# omar = BankAccount(0.02, 30900)
# omar.deposit(200).deposit(600).withdraw(611).withdraw(811).withdraw(666).withdraw(111).yield_interest().display_account_info()








ibraheem = User("mhammad", "ali@3.com")
saad = User("mhrrad", "yli@3.com")
ibm = User("mhamqq", "afi@3.com")

# ibraheem.make_deposit(1000).make_deposit(100).make_deposit(1300).make_withdrawal(1300).display_user_balance()

# saad.make_deposit(10).make_deposit(11).make_withdrawal(1).make_withdrawal(6).display_user_balance()

# ibm.make_deposit(170000).make_withdrawal(17000).make_withdrawal(10000).make_withdrawal(1000).display_user_balance()


# ibraheem.transfer_money(1000, saad).display_user_balance()
# saad.display_user_balance()




