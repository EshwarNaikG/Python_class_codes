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
        

