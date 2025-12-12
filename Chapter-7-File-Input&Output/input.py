f = open("D:\PYTHON FULL STACK WEB DEVELOPER\PYTHON CLASS BY APNA COLLEGE\Chapter-7-File-Input&Output\demo.txt","r")

# READING A FILE:- 

# Reading the complete file

# data=f.read()
# print(data)
# print(type(data))
# # f.close()

#--------------------------
# data=f.read(5)
# print(data)

#--------------------------
# reading line by line

# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)

#------------------------------------------------------------------------------------------------------

# WRITTING A FILE:-

# f = open("D:\PYTHON FULL STACK WEB DEVELOPER\PYTHON CLASS BY APNA COLLEGE\Chapter-7-File-Input&Output\demo.txt","w")
# f.write("This is a new line")   # write mode overwrites the entire content of the file
# f.close()

# f = open("D:\PYTHON FULL STACK WEB DEVELOPER\PYTHON CLASS BY APNA COLLEGE\Chapter-7-File-Input&Output\demo.txt","a")
# f.write(" \nThis line is appended")  # append mode adds content to the end of the file 


# f = open("D:\PYTHON FULL STACK WEB DEVELOPER\PYTHON CLASS BY APNA COLLEGE\Chapter-7-File-Input&Output\demo.txt","a")
# f.write(" \nFull stack web developer")  # append mode adds content to the end of the file 

# f.close()

#--------------------------

# f= open("sample.txt", "w")
# f.write("Hello, World!\n")
# f.write("Welcome to file handling in Python.\n")
# f.write("Hi My name is Eshwar Naik G\n")
# f.close()

#--------------------------

# f = open("example.txt", "a")
# f.write("This is an appended line.\n")
# f.write("Hi My name is Eshwar Naik G\n")
# f.close()

#-------------------------------------------------------------------------------------------------------


# WITH SYNTAX:-

# with open("example.txt", "r") as f:
#     data = f.read()
#     print(data )



# with open("example.txt", "w") as f:
#     f.write("This file has been overwritten using 'with' syntax.\n")
#     f.write("Hi My name is Eshwar Naik G\n")


# with open("example.txt", "a") as f:
#     f.write("This line has been appended using 'with' syntax.\n")
#     f.write("Hi My name is Eshwar Naik G\n")

#-------------------------------------------------------------------------------------------------------

# IMPORTING OS MODULE:-

# import os
# os.remove("example.txt")  # This will delete the file named example.txt


class Bank_Account:
	def __init__(self, account_number, account_holder, balance):
		self.account_number = account_number
		self.account_holder = account_holder
		self.balance = balance
	def deposit(self, amount):
		self.balance += amount
		print(f"Deposited: {amount}. New Balance: {self.balance}")
	def withdra(self, amount):
		if amount > self.balance:
			print("Insufficient balance")
		else:
			self.balance -= amount
			print(f"Withdra: {amount}, new balance: {self.balance}")
	def account_info(self):
		print(f"account number {self.account_number}, account holder name: {self.account_holder}, balance: {self.balance} ")
bank_account1 = Bank_Account(1234567, "Eshwara Naik G", 100000)
bank_account1.account_info()