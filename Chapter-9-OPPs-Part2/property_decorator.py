# Property decorator :
""" We use @property decorator on any method in the class to use the method as a property """

#Example:

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
    
s1 = Student(98, 99, 97)
print(s1.percentage)

s1.phy = 86
print(s1.percentage)