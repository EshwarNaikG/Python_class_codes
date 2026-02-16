# Abstraction in Python OOP
""" Hiding the complex implementation details and showing only the essential features of the object is called Abstraction.
It helps in reducing programming complexity and effort."""

# OR
""" Hiding the  implementation details of a class and only showing the essential features to the user
is called abstraction"""

#example of Abstraction 

class Car:
    def __init__(self):
        self.acceleration = False
        self.braking = False
        self.clutch = False

    def start(self):
        self.acceleration = True
        self.braking = False
        self.clutch = True
        print("Car started")

    def stop(self):
        self.acceleration = False
        self.braking = True
        self.clutch = False
        print("Car stopped")

# Creating an object of the Car class
my_car = Car()
my_car.start()  # Output: Car started
my_car.stop()   # Output: Car stopped

""" In the above example, the complex implementation details of starting and stopping the car
are hidden from the user. The user only needs to know how to use the start() and stop() methods to operate the car. 
This is an example of abstraction in Python OOP."""


# Another example of Abstraction
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass    
class Dog(Animal):
    def sound(self):
        return "Woof"   
class Cat(Animal):
    def sound(self):
        return "Meow"
dog = Dog()
cat = Cat()
print(f"Dog Sound: {dog.sound()}")  # Output: Dog Sound: Woof
print(f"Cat Sound: {cat.sound()}")  # Output: Cat Sound: Meow


#------------------------------------------------------------------------

#What is Encapsulation in Python OOP?
""" Encapsulation is the process of wrapping data and methods into a single unit called class."""

# Example of Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private attribute
        self.__balance = balance                  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid withdrawal amount")

    def get_balance(self):
        return self.__balance
    
# Creating an object of the BankAccount class
account = BankAccount("123456789", 1000)
account.deposit(500)          # Output: Deposited: 500
account.withdraw(200)         # Output: Withdrew: 200
print(f"Current Balance: {account.get_balance()}")  # Output: Current Balance: 1300
# Trying to access private attributes directly will raise an AttributeError
# print(account.__balance)    # Uncommenting this line will raise an error  

""" In the above example, the account number and balance attributes are private 
and cannot be accessed directly from outside the class."""