# del Keyword in python
"""del keyword used to delete object propeties or object itself """

# Example:-
# del s1.name       --- This is used to delete object properties
# del s1           ---- This is used to delete object itself

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Eshwar")
print(s1.name) 

# del keyword
del s1

print(s1.name)   # NameError: name 's1' is not defined