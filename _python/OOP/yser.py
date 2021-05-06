class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
    def make_deposit(self, ammount):
        self.balance = self.balance + ammount

    def make_withdrawal(self, ammount):
        self.balance = self.balance - ammount

    def display_user_balance(self):
        print(f"user: {self.name}, balance: {self.balance}")

    def transfer_money(self, ammount, person):
        self.make_withdrawal(ammount)
        person.make_deposit(ammount)

ibraheem = User("mhammad", "ali@3.com")
saad = User("mhrrad", "yli@3.com")
ibm = User("mhamqq", "afi@3.com")

ibraheem.make_deposit(1000).make_deposit(100).make_deposit(1300).make_withdrawal(1300).display_user_balance()

saad.make_deposit(10).make_deposit(11).make_withdrawal(1).make_withdrawal(6).display_user_balance()

ibm.make_deposit(170000).make_withdrawal(17000).make_withdrawal(10000).make_withdrawal(1000).display_user_balance()


ibraheem.transfer_money(1000, saad).display_user_balance()
saad.display_user_balance()




