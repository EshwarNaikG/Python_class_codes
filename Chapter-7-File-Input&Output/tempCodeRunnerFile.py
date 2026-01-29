
# def account_info(self):
# 	print(f"account number {self.account_number}, account holder name: {self.account_holder}, balance: {self.balance} ")
# bank_account1 = Bank_Account(1234567, "Eshwara Naik G", 100000)
# bank_account1.account_info()



class Bank_Account:
	def __init__(self, account_number, account_holder, balance):
		self.account_number = account_number
		self.account_holder = account_holder
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		print(f"deposited {amount}, new balance {self.balance}")

	def withdra(self, amount):
		if amount > self.balance:
			print("Insufficient balance")
		else:
			self.balance -=amount
			print(f"withdra {amount}, new balance {self.balance}")

	def acount_info(self):
		print(f"account number {self.account_number}, account holder name {self.account_holder}, balance {self.balance}")
bank_account1 = Bank_Account(1234567, "Eshwara Naik G", 100000)
bank_account1.acount_info()
bank_account1.deposit(5000)
bank_account1.withdra(2000)
bank_account1.withdra(200000)
bank_account1.acount_info()