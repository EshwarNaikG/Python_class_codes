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

