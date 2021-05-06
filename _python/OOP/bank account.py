class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = 0.01
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

ibraheem = BankAccount(0.01, 1000)
ibraheem.deposit(1900)
ibraheem.withdraw(900)
ibraheem.display_account_info()
ibraheem.yield_interest()
ibraheem.display_account_info()

Mahmoud = BankAccount(0.03, 55000)
Mahmoud.deposit(200).deposit(700).deposit(600).withdraw(2000).yield_interest().display_account_info()

omar = BankAccount(0.02, 30900)
omar.deposit(200).deposit(600).withdraw(611).withdraw(811).withdraw(666).withdraw(111).yield_interest().display_account_info()
