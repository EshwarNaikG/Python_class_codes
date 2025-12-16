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