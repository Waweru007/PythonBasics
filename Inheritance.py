class Account: ##This is the parent class which will be inherited by the child classes
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

class PersonalAccount(Account): ##The first child class(SubClass)
     def atm_withdraw(self, amount):
         if self.balance < amount:
             print("Insufficient Balance")
         else:
             self.balance = self.balance - (amount+30)


class SaccoAccount(Account): ##Sacco is inheriting from account class
    def atm_withdraw(self, amount):
        if self.balance < (amount+1000):
            print("Insufficient Balance")
        else:
            self.balance = self.balance - (amount + 100)
    def withdraw(self, amount):#This is an overwrit=ding code that overides the first code
        if self.balance < amount:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - (amount+100)


# ac1=PersonalAccount("henry",10001, 20000)
#
# ac1.withdraw(2000)
# ac1.check()
# ac1.atm_withdraw(2000)
# ac1.check()

saccount=SaccoAccount("Miky", 10002, 20000)
saccount.check()
saccount.withdraw(200)
saccount.check()
saccount.atm_withdraw(19000)

