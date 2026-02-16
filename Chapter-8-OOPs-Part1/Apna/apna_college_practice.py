#1. Create student class that takes name and marks of 3 subjects as arguments in constructor.
# then create a method to print average marks of the student.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # marks is expected to be a list of 3 subjects' marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Eshwar", [85, 90, 95])
print(f"{s1.name}'s average marks: {s1.average_marks()}")

s2 = Student("Adithya", [80, 88, 92])
print(f"{s2.name}'s average marks: {s2.average_marks()}")


# output:# Eshwar's average marks: 90.0
# Adithya's average marks: 86.66666666666667

# OR

class Student:
    def __init__(self, name, marks):  # 

        self.name = name
        self.marks = marks  # marks is expected to be a list of 3 subjects' marks

    def get_avg_marks(self):     # method to calculate average marks
        total = 0
        for mark in self.marks:
            total += mark
        average = total / len(self.marks)
        return average
    
s1 = Student("Eshwar", [99, 98, 97])   # Creating object
print(f"{s1.name}'s average marks: {s1.get_avg_marks()}")  # Calling the method

s1.name = "adithya"
print(f"{s1.name}'s average marks: {s1.get_avg_marks()}")  # Calling the method

# output: Eshwar's average marks: 98.0

#-------------------------------------------------------------------------------------------------


        