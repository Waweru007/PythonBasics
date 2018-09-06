class Account:
    def __init__(self, names, account_no, balance):
        self.names=names
        self.account_no=account_no
        self.balance=balance
    def check(self):
        print(self.names,self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw (self, amount):
        if self.balance<amount:
            print("Insufficient Balance")
        else:
            self.balance=self.balance-amount


p1=Account("Mike",101,2000)
p2=Account("John",102,2020)

p1.check()
p1.deposit(200)
p1.check()
p1.withdraw(6000)
p1.check()
p2.check()
p2.deposit(200)
p2.check()
p2.withdraw(4000)



