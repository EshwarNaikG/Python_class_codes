# Private Attributes & Methods :
# Conceptual Implementations in Python
""" Private attributes & methods are meant to be used only within the class 
and are not accessible from  outside the class """

# Note :- Private attributes & methods are created using __(underscore) symboles.


#Public Attributes :
class Student:
    def __init__(self, name):
        self.name = name      # Public attributes 

s1 = Student("Eshwar")
# print(s1.name)

# Private Attributes :
# example-1

class Car:
    def __init__(self, name):
        self.__name = name       # Private attributes

car1 = Car("Maruthi")
# print(car1.name)

# Example-2

class Account:
    def __init__(self, account_no, Password):
        self.account_no = account_no       # Public Attribute
        self.__password = Password         #Private Attribute 

    def reset_password(self):
        print(self.__password)

account1 = Account(12345,"1993")
print(account1.account_no)     # Output - 12345
# print(account1.__password)     # 'Account' object has no attribute '__password'

print(account1.reset_password())  # call to reset_password function  Output - 1993
        