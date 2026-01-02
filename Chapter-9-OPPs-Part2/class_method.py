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