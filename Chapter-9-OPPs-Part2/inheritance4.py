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