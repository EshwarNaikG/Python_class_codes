#what is OOP?
""" OOP is a programming paradigm that uses "objects" to design software."""

"""OOP (Object-Oriented Programming) is a programming paradigm that organizes code into objects 
that contain data (attributes) and behavior (methods).
"""


# What is class in Python?
""" A class is a blueprint for creating objects. It defines a set of attributes and methods that
an object created from the class will have.
"""
# Creating a class in Python
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
#--------------------------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------------------


    

