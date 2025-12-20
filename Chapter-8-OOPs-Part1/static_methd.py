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