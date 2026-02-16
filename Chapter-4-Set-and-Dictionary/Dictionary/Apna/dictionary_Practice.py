# 1. Store following word meaning in a python dictionary :
my_dict = {
    "table" : ["A piece of furniture", "list of facts and figures"] ,
    "cat" : "a small animal"
}

print(my_dict)

#-----------------------------------------------------------------------------------------------

# 2. You are given a list of subjects for students. Assume 1 class room is required for 1 subject.
# How many class romms are need by all students.

class_rooms = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}

print(class_rooms)
print(len(class_rooms))

#------------------------------------------------------------------------------------------------

# 3. WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#  start with an empty dictionary & add one by one.
#  Use subject name as key & marks as value

marks = {}  # empty dictionary

x = int(input("enter phy marks : "))  # User input
marks.update({"phy" : x})

y = int(input("enter chem marks : ")) # User input
marks.update({"chem" : y})

z = int(input("enter maths marks :")) # User input
marks.update({"maths" : z})

print(marks)


#-----------------------

student_marks = {}  # empty dictionary

x = int(input("enter phy marks : "))  # User input
student_marks.update({"phy" : x})

x = int(input("enter chem marks : ")) # User input
student_marks.update({"chem" : x})

x = int(input("enter maths marks :")) # User input
student_marks.update({"maths" : x})

print(student_marks)

#---------------------------------------------------------------------------------------------
# 4. Figure out a way to store 9 & 9.0 as separate values in the set.
# ( you can take help of built-in data types)

Values = {
    ("float" , 9.0),
    ("int", 9)
}

print(Values)