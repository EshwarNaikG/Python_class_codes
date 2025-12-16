# Class & Instance Attributes ( attributes means data)
# 2 Types
# 1. Class Attributes  2. Object or Instance Attributes

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