#!/usr/bin/python3

class bank:
    def __init__(self, balance):
        self.balance = balance

    def checkbalace(self):
        print(self.balance)

    def withdara(self, amount):
        self.amount = amount
        if self.balance < self.amount:
            print("Not Enough Balance")
        else:
            self.balance = self.balance - self.amount
            print(self.balance)

    def credit(self, amount):
        self.amount = amount
        self.balance = self.amount + self.balance
        print(self.balance)


a = bank(100)
a.withdara(10)
a.credit(100)
a.checkbalace()
