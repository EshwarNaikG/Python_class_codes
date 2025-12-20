# What is encapsulation in python ?
"""Encasulation is the process of wrapping data and methods into a single unit called class"""

# practice :- create a account class  with 2 attributes  balance and account_number
# creat methods for debit, credit and print the balance.

class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("RS.",amount ,"was debited")
        print("Total balance= ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("RS.",amount ,"was credited")
        print("Total balance= ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000,1234)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(5000)


        