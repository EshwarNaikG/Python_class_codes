# CLASS METHOD:-

# class method :
""" A class method is bound to the  class & receives the class as an implicit first argument"""

# Note :- static method can't access or modify class state  & generally for utility.

# Example:

class Student:
    @classmethod
    def college(cls):  # refers to the class
        pass

#------------------------------------------------------------------------
# Example-2

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Eshwar")
print(p1.name)
print(Person.name)

#----------------------------------------------------------------------------------

# 1. static method()  ==> No attributes access
# 2. class method(cls)   ==> use and access class attributes
# 3. instance method(self) ==> Use and access instance attributes

#========================================================================================================
# Private Attributes & Methods :
# Conceptual Implementations in Python
""" Private attributes & methods are meant to be used only within the class 
and are not accessible from  outside the class """


# Note :- Private attributes & methods are created using __(underscore) symboles.

# Private Methods:
#Example-1

# class Person:
#     __name = "anonymous"    #private attributes

#     def __hello():     # Private methods
#         print("hello Person!")
# p1 = Person()

#Private attributes & Private methods calling from outside the class
# print(p1.__name)

# print(p1.__hello())

#------------------------------------------------------------------------------------

#Example-2
class Person:
    __name = "anonymous"    # Private attributes

    def __hello(self):   # Private method
        print("Hello Person!")

    def welcome(self):   # Public method
        self.__hello()   #class method calls to private method  only within the class.
        print(self.__name) # class method calls to private attribute only within the class.

p1 = Person()
print(p1.welcome())  # Object calls public methods from outside the class
# Note :- Private methods access only inside the class function.
# Private methos & Attributes are not accessible from outside the class
#------------------------------------------------------------------------------------


#=======================================================================================================

# PRIVATE ATTRIBUTES :-

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
        
#================================================================================================

# INHERITANCE :

# What is inheritance in python ?
"""When one class derives the properties and methods of another class is called inheritance.
OR
When child class derives the properties and methods of parent class is called inheritance. """

# Types of Inheritance - 3:
"""
1. Single Inheritance
2. Multi-level Inheritance
3. Multiple Inheritance
"""
#---------------------------------------------------------------------------------------------------
# 1. Single Inheritance :
# Example :

class Car:           # Parent class or Base class
    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):          # Child class inherit Parent class
    def __init__(self, name, color):
        self.name = name
        self.color = color

car1 = ToyotaCar("Fortune", "Black")
# car2 = ToyotaCar("Perius", "Red")

# print(car1.name, car1.color, car1.start(), car1.stop())
# print(car2.name, car2.color, car2.start(), car2.stop())

#--------------------------------------------------------------------------------------------------
# 2. Multi-Level Inheritance :

class Car:           # Parent class or Base class
    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):          # Child class inherit Parent class
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):      # child class
    def __init__(self, type):
        self.type = type

# car1 = Fortuner("diesel")
# car1.start()

#-----------------------------------------------------------------------------------------

# 3. Multiple Inheritance:

class A:       # Parent class - 1
    varA = "Welcome to class A"   

class B:       # Parent class - 2
    varB = "Welcome to class B"

class C(A, B):  # Child class- C derived both parent class A & B
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)

#=================================================================================================

# SUPER METHOD :
 # Super Method :
""" Super() method is used to access methods of the parent class """

# Example:

class Car:           # Parent class or Base class
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):          # Child class derived  Parent class
    def __init__(self, name, type):
        super().__init__(type)      #super() method is used access methods of the parent class
        super().start()             # super method access parent class methods
        super().stop()               # super method access parent class methods
        self.name = name
      
car1 = ToyotaCar("Fortune", "Electric")
print(car1.type)
print(car1.name)

#===============================================================================================

# PROPERTY DECORATOR :

# Property decorator :
""" We use @property decorator on any method in the class to use the method as a property """

#Example:

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
    
s1 = Student(98, 99, 97)
print(s1.percentage)

s1.phy = 86
print(s1.percentage)

#============================================================================================

# DEL KEYWORD :-

# del Keyword in python
"""del keyword used to delete object propeties or object itself """

# Example:-
# del s1.name       --- This is used to delete object properties
# del s1           ---- This is used to delete object itself

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Eshwar")
print(s1.name) 

# del keyword
del s1

print(s1.name)   # NameError: name 's1' is not defined