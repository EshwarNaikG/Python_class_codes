#what is OOP in python ?
"""OOP (Object-Oriented Programming) is a programming paradigm that organizes code into objects 
that contain data (attributes) and behavior (methods).
"""
# What is class in Python?
""" A class is a blueprint for creating objects. It defines a set of attributes and methods that
an object created from the class will have.
"""

# Creating a class in Python

# Example-1:-
class Student:
    # attributes
    name = "Eshwar Naik G"
    age = 21
    course = "Full Stack Web Development"
    # method
    def student_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")
# Creating an object of the class
student1 = Student()
# Accessing attributes and methods of the object
print(student1.name)  # Output: Eshwar Naik G
print(student1.age)   # Output: 21
print(student1.course)  # Output: Full Stack Web Development

student1.student_info()  # Output: Name: Eshwar Naik G, Age: 21, Course: Full Stack Web Development

# Example-2:-
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def employee_info(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

# Creating an object of the Employee class
employee1 = Employee("Eshwar Naik G", "Software Engineer", 60000)
employee1.employee_info() # Output: Name: Eshwar Naik G, Position: Software Engineer, Salary: 60000

employee2 = Employee("Adithya", "Data Scientist", 75000)
employee2.employee_info() # Output: Name: Alice Smith, Position: Data Scientist, Salary: 75000


# Example-3:- 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def car_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Creating an object of the Car class
car1 = Car("Toyota", "Camry", 2020)
car1.car_info()  # Output: Car Make: Toyota, Model: Camry, Year: 2020

car2 = Car("Honda", "Civic", 2019)
car2.car_info()  # Output: Car Make: Honda, Model: Civic, Year: 2019

car3 = Car("Ford", "Mustang", 2021)
car3.car_info()  # Output: Car Make: Ford, Model: Mustang, Year: 2021


# Example-4:-
class Bank_Acount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")
    def account_info(self):
        print(f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}")

bank_account1 = Bank_Acount("123456789", "Eshwar Naik G", 1000)
bank_account1.account_info()  # Output: Account Number: 123456789, Account Holder: Eshwar Naik G, Balance: 1000
bank_account1.deposit(500)    # Output: Deposited: 500. New Balance: 1500
bank_account1.withdraw(200)   # Output: Withdrew: 200. New Balance: 1300
bank_account1.withdraw(2000)  # Output: Insufficient funds  

bank_account2 = Bank_Acount("987654321", "Adithya", 2000)
bank_account2.account_info()  # Output: Account Number: 987654321, Account Holder: Adithya, Balance: 2000
bank_account2.deposit(1000)   # Output: Deposited: 1000. New Balance: 3000
bank_account2.withdraw(500)    # Output: Withdrew: 500. New Balance: 2500
bank_account2.withdraw(4000)  # Output: Insufficient funds

#======================================================================================================

# ATTRIBUTES :-
"""2 Types"""
"""
1. Class Attributes  2. Object or Instance Attributes
"""

#1. Class Attributes :
"""Class attributes are commom for all objects"""

#2. Object Attributs :
""" Object attribute is different for different object"""

# Example

class Student:
    college_name = "VVIET"     # Class attribute

    def __init__(self, name, marks):
        self.name = name       # object attribute
        self.marks = marks     # object attribute

s1 = Student("Eshwar", 99)
print(f"college Name : {s1.college_name}, Student Name : {s1.name}, Marks : {s1.marks}" )

s2 = Student("Adithya", 98)
print(f"college Name : {s2.college_name}, Student Name : {s2.name}, Marks : {s2.marks}" )


#===============================================================================================

# CONSTRUCTOR :- 

# what is constructor in python ?


# Types of constructor in python --- 2
# 1. Default constructor  2. Parameterized constructor


class Student:
    def __init__(self):   # default constructor
        pass

    def __init__(self, name, age): # parameterized constructor
        self.name = name
        self.age = age

s1 = Student("Eshwar", 30)  # creating object 1
print(s1.name, s1.age)

s2 = Student("Adithya", 2)  # creating object 2
print(s2.name, s2.age)


#================================================================================================

# INIT_FUNCTION (__init__()) :-

# --init-- Function in Python OOP
""" --init-- function is executed automatically when an object of a class is created.
It is used to initialize the attributes of the class.
"""

class Student:          # Defining the Student class
    def __init__(self, fullname):   # The --init-- method with fullname parameter
        self.fullname = fullname
        print("Adding a new student in the database.")
        print(f"Student Name: {self.fullname}")
    
# Creating an object of the Student class
student1 = Student("Eshwar Naik G") 
student2 = Student("Adithya")
print(student1.fullname)


# what is self parameter in python ?
""" The self parameter is a reference to the current instance of the class,
and it is used to access variables that belongs to the class"""


#=================================================================================================

# ENCASULATION :- 

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



#========================================================================================================

# METHODS :-

# What is methoods in Python?
""" Methods  are functoins that belongs to objects.
They are used to define the behaviors of an object."""

# Types of Methods in Python OOP
# 1. Instance Methods
# 2. Class Methods
# 3. Static Methods
# 4. Special Methods

#_________________________________________________________________________________________________

# 1. Instance Methods :
""" Instance methods are the most common type of methods in Python OOP.
 They operate on the instance of the class (object) and can access and modify the object's attributes."""

# Example of Instance Method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):   # Instance Method
        print(f"Student Name: {self.name}, Age: {self.age}")

s1 = Student("Eshwar", 30)
s1.display_info()  # Calling the instance method

#output: Student Name: Eshwar, Age: 30

#_________________________________________________________________________________________________

# 2. Class Methods :
""" Class methods are methods that are bound to the class rather than the instance of the class.
 They can access and modify class-level attributes."""

class Student:
    school_name = "VVIET"   # Class Attribute

    @classmethod
    def display_school(cls):   # Class Method
        print(f"School Name: {cls.school_name}")
Student.display_school()  # Calling the class method

#output: School Name: VVIET

#_________________________________________________________________________________________________

# 3. Static Methods :
""" Static methods are methods that do not operate on an instance or class. 
They are utility functions that belong to the class namespace."""

class MathOperations:
    @staticmethod
    def add(a, b):   # Static Method
        return a + b
result = MathOperations.add(5, 3)  # Calling the static method
print(f"Addition Result: {result}")

#output: Addition Result: 8

#_________________________________________________________________________________________________
# 4. Special Methods :
""" Special methods, also known as magic methods or dunder methods, are predefined methods in Python 
that have double underscores at the beginning and end of their names.
They are used to define the behavior of objects for built-in operations."""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):   # Special Method
        return f"Point({self.x}, {self.y})" 
p1 = Point(2, 3)
print(p1)  # Calling the special method __str__ 

#output: Point(2, 3)

#_________________________________________________________________________________________________


# Summary :
""" Methods in Python OOP are functions that define the behaviors of objects.
There are four main types of methods: instance methods, class methods, static methods, and special methods.
Each type serves a different purpose and operates at different levels within the class structure."""

#_________________________________________________________________________________________________


# Apna college youtube link for more details :

#example: Methods

class Student:
    def __init__(self, name):   #constructor method
        self.name = name

    def hello(self):   # instance method
        print(f"Hello, my name is {self.name}")
    
student1 = Student("Eshwar")
student1.hello()  # Calling the instance method

#output: Hello, my name is Eshwar

#_________________________________________________________________________________________________

class student:
    school_name = "VVIET"   # class attribute
    def __init__(self, name, marks):   # constructor method
        self.name = name
        self.marks = marks
    
    def welcome(self):
        print(f"Welcome {self.name}")

    def get_marks(self):
        return self.marks
    
s1 = student("Eshwar", 99)
s1.welcome()  # Calling instance method
print(f"{s1.name} scored {s1.get_marks()} marks")  # Calling instance method

#output:
# Welcome Eshwar
# Eshwar scored 99 marks

#_________________________________________________________________________________________________
        
# STATIC METHOD :-

# Example of Static Method in Python OOP
class Student:
    school_name = "ABC High School"

    @staticmethod
    def get_school_name():
        return Student.school_name
    
s1 = Student()
print(f"School Name: {s1.get_school_name()}")


# output: School Name: ABC High School

#--------------------------------------------------------------------------------------------
#2nd Example

class Student:
    @staticmethod
    def college():
        print("VVIET")

Student.college()
# output: VVIET
# OR
s1 = Student()
s1.college()
# output: VVIET
#--------------------------------------------------------------------------------------------
#3rd Example
class Calculator:
    @staticmethod
    def multiply(x, y):
        return x * y
result = Calculator.multiply(4, 5)
print(f"Multiplication Result: {result}")

# output: Multiplication Result: 20

#--------------------------------------------------------------------------------------------

#4th Example
class Circle:
    pi = 3.14159

    @staticmethod
    def area(radius):
        return Circle.pi * radius * radius  
area_of_circle = Circle.area(5)
print(f"Area of Circle: {area_of_circle}")



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#=========================================================================================================

# 🧱 Python OOPS Notes (Object-Oriented Programming)

"""Object-Oriented Programming (OOP) is a programming paradigm based on objects and classes."""

# 📌 1. What is OOP?
"""OOP (Object-Oriented Programming) is a programming paradigm that organizes code into objects 
that contain data (attributes) and behavior (methods).
"""

"""
Class
Object
Abstraction
Encapsulation
Inheritance
Polymorphism
"""
# 🏗 2. Class and Object
# 🔹 Class :-
"""Class is a blueprint for creating an objects"""
# 🔹 Object :-
"""Object is an instance of a class"""

# ✅ Example:-1
class Student:   # creating class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}  my age is {self.age}")

# Creating object
s1 = Student("Eshwar", 22)
s1.greet()


# 🔑 3. Constructor (__init__) :-
"""
#. Special method
#. Automatically called when object is created
"""
# def __init__(self):
    # initialization code


# 🔒 4. Encapsulation  :- 
"""Binding data and methods together in a single unit (class)."""

# Access Modifiers in Python:
"""
| Type      | Syntax | Meaning                   |
| --------- | ------ | ------------------------- |
| Public    | var    | Accessible everywhere     |
| Protected | _var   | Internal use (convention) |
| Private   | __var  | Name mangled              |

"""
# Example-1 :-
class Bank:
    def __init__(self):
        self.name = "Eshwar"        # Public
        self._balance = 1000       # Protected
        self.__pin = 1234          # Private

    def get_pin(self):
        return self.__pin


# 🎭 5. Abstraction :-
"""Hiding implementation details and showing only functionality."""
# Using abc module:
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# 👨‍👦 6. Inheritance :-
"""One class inherits properties of another."""
# Types of Inheritance:
"""
1. Single
2. Multiple
3. Multilevel
4. Hierarchical
5. Hybrid
"""

# Example-1 :
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()


# 🔄 7. Polymorphism :-
"""Same method name, different behavior."""

# 🔹 Method Overriding
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# 🔹 Operator Overloading
print(5 + 3)        # 8
print("Hi " + "All")  # Hi All


# 🧬 8. super() Function :- 
"""Used to call parent class constructor or methods."""
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

# 🧠 9. Class Variables vs Instance Variables :-
class Employee:
    company = "TCS"   # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable


# 🛠 10. Special (Magic / Dunder) Methods :-
"""
| Method     | Purpose               |
| ---------- | --------------------- |
| `__init__` | Constructor           |
| `__str__`  | String representation |
| `__len__`  | Length                |
| `__add__`  | Addition              |
| `__del__`  | Destructor            |

"""
# Example 
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"Book with {self.pages} pages"


# 🧩 11. Composition :-
"""Class inside another class"""
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

c = Car()
c.engine.start()

# 📚 12. Method Types in Python :-
"""
| Type            | Decorator     |
| --------------- | ------------- |
| Instance Method | default       |
| Class Method    | @classmethod  |
| Static Method   | @staticmethod |

"""
# Example 
class Demo:
    @classmethod
    def class_method(cls):
        print("Class method")

    @staticmethod
    def static_method():
        print("Static method")


# ⚖ 13. OOP vs Procedural Programming :-
"""
| OOP                 | Procedural         |
| ------------------- | ------------------ |
| Based on objects    | Based on functions |
| Secure              | Less secure        |
| Reusable            | Less reusable      |
| Real-world modeling | Linear flow        |

"""
# 🎯 14. Interview Important Questions :-
"""
1. What is OOP?

2. What are 4 pillars of OOP?

3. Difference between class and object?

4. What is encapsulation?

5. What is abstraction?

6. Difference between inheritance and composition?

7. What is polymorphism?

8. What is method overriding?

9. What is super()?

10. Difference between class and static method?
"""

# 🔥 Quick Revision Summary :
"""
✔ Class = Blueprint
✔ Object = Instance
✔ 4 Pillars → Encapsulation, Abstraction, Inheritance, Polymorphism
✔ Use super() for parent access
✔ Python supports multiple inheritance
✔ Everything in Python is object
"""

































